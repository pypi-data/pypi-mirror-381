import requests
import aiohttp
import asyncio
from time import sleep
from .exceptions import TranslationError, NetworkError, EmptyTextError

class Translator:
    BASE_URL = "https://translate.googleapis.com/translate_a/single"

    def __init__(self, default_dest="en", retries=3, delay=1, cache_enabled=True):
        self.default_dest = default_dest
        self.retries = retries
        self.delay = delay
        self.cache_enabled = cache_enabled
        self._cache = {}

    def translate(self, text, src="auto", dest=None, return_detected_lang=False):
        """
        متن یا لیست متن‌ها رو ترجمه کن، می‌تونه sync یا await باشه.
        """
        dest = dest or self.default_dest

        # اگر متن لیست هست، هر کدوم رو ترجمه کن
        if isinstance(text, list):
            return [self._translate_item(t, src, dest, return_detected_lang) for t in text]
        # اگر متن یک رشته است
        return self._translate_item(text, src, dest, return_detected_lang)

    def _translate_item(self, text, src, dest, return_detected_lang=False):
        # اگر dest لیست است، برای هر زبان جدا ترجمه کن
        if isinstance(dest, list):
            return {d: self._translate_single(text, src, d, return_detected_lang) for d in dest}
        return self._translate_single(text, src, dest, return_detected_lang)

    def _translate_single(self, text, src, dest, return_detected_lang=False):
        if not text.strip():
            raise EmptyTextError("متن خالی است / Empty text")

        cache_key = (text, src, dest)
        if self.cache_enabled and cache_key in self._cache:
            return self._cache[cache_key]

        params = {"client": "gtx", "sl": src, "tl": dest, "dt": "t", "q": text}

        for attempt in range(1, self.retries + 1):
            try:
                resp = requests.get(self.BASE_URL, params=params, timeout=10)
                resp.raise_for_status()
                data = resp.json()
                translated = "".join([seg[0] for seg in data[0]])
                detected = data[2] if len(data) > 2 else src
                result = {"translation": translated, "detected_lang": detected} if return_detected_lang else translated
                if self.cache_enabled:
                    self._cache[cache_key] = result
                return result
            except requests.exceptions.RequestException as e:
                if attempt == self.retries:
                    raise NetworkError(f"❌ Network error: {e}")
                sleep(self.delay)
            except Exception as e:
                raise TranslationError(f"❌ Translation failed: {e}")

    async def atranslate(self, text, src="auto", dest=None, return_detected_lang=False):
        """
        نسخه async ترجمه متن یا لیست متن‌ها
        """
        dest = dest or self.default_dest

        if isinstance(text, list):
            return [await self._atranslate_item(t, src, dest, return_detected_lang) for t in text]
        return await self._atranslate_item(text, src, dest, return_detected_lang)

    async def _atranslate_item(self, text, src, dest, return_detected_lang=False):
        if isinstance(dest, list):
            results = {}
            for d in dest:
                results[d] = await self._atranslate_single(text, src, d, return_detected_lang)
            return results
        return await self._atranslate_single(text, src, dest, return_detected_lang)

    async def _atranslate_single(self, text, src, dest, return_detected_lang=False):
        if not text.strip():
            raise EmptyTextError("متن خالی است / Empty text")

        cache_key = (text, src, dest)
        if self.cache_enabled and cache_key in self._cache:
            return self._cache[cache_key]

        params = {"client": "gtx", "sl": src, "tl": dest, "dt": "t", "q": text}

        for attempt in range(1, self.retries + 1):
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(self.BASE_URL, params=params, timeout=10) as resp:
                        if resp.status != 200:
                            raise NetworkError(f"HTTP {resp.status}")
                        data = await resp.json()
                        translated = "".join([seg[0] for seg in data[0]])
                        detected = data[2] if len(data) > 2 else src
                        result = {"translation": translated, "detected_lang": detected} if return_detected_lang else translated
                        if self.cache_enabled:
                            self._cache[cache_key] = result
                        return result
            except Exception as e:
                if attempt == self.retries:
                    raise TranslationError(f"❌ Async translation failed: {e}")
                await asyncio.sleep(self.delay)
