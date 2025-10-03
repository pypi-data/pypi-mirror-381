import requests
import aiohttp
import asyncio
from time import sleep
from .exceptions import TranslationError, NetworkError, EmptyTextError

class Translator:
    BASE_URL = "https://translate.googleapis.com/translate_a/single"

    def __init__(self, default_dest="en", retries=3, delay=1, cache_enabled=True):
        """
        :param default_dest: Default target language / زبان مقصد پیش‌فرض
        :param retries: Number of retries in case of failure / تعداد تلاش دوباره
        :param delay: Delay between retries in seconds / فاصله بین تلاش‌ها
        :param cache_enabled: Enable internal cache / فعال بودن کش داخلی
        """
        self.default_dest = default_dest
        self.retries = retries
        self.delay = delay
        self.cache_enabled = cache_enabled
        self._cache = {}

    def translate(self, text, src="auto", dest=None, return_detected_lang=False):
        """
        Translate text (sync or async if awaited)

        ترجمه متن، هوشمندانه: در حالت عادی sync، در حالت await async
        """
        dest = dest or self.default_dest

        if asyncio.iscoroutinefunction(self._translate_single):
            return self._atranslate_single(text, src, dest, return_detected_lang)
        else:
            return self._translate_single(text, src, dest, return_detected_lang)

    # -------------------------- Sync --------------------------
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

    # -------------------------- Async --------------------------
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
