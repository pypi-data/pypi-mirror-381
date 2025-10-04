import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from colorama import Fore, init
import threading
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
init(autoreset=True)

fr = Fore.RED
fw = Fore.WHITE
fg = Fore.GREEN

class h0rn3t:
    """
    Threaded path scanner that writes hits to a file.
    Usage:
        scanner = h0rn3t(sites_file, paths, check_texts, threads=10, output_file="results.txt")
        scanner.run()
    """

    def __init__(self, sites_file, paths, check_texts, threads=10, output_file="BADS_OK.txt", timeout=15, verify_ssl=False):
        self.sites_file = sites_file
        self.sites = self._load_sites(sites_file)
        self.paths = paths or []
        self.check_texts = [t.lower() for t in (check_texts or [])]
        self.threads = max(1, int(threads))
        self.output_file = output_file
        self.timeout = timeout
        self.verify_ssl = verify_ssl
        self._file_lock = threading.Lock()
        self._session = requests.Session()
        # A small default header
        self._session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'})
        # allow caller to override session if needed
        self._stop_on_first = False

    def _load_sites(self, filename):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                return [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            print(f"{fr} File not found: {filename}")
            return []

    def _check_url(self, base, path):
        url = base.rstrip("/") + "/" + path.lstrip("/")
        try:
            resp = self._session.get(url, headers=self._session.headers , timeout=self.timeout, verify=self.verify_ssl)
            text = resp.text or ""
            low = text.lower()
            for keyword in self.check_texts:
                if keyword and keyword in low:
                    self._write_result(url)
                    print(f"{fw} BADS : {base} {fg}--> VULN")
                    return True
            # not vulnerable (or keyword not found)
            print(f"{fw} BADS : {base} {fr}--> NO")
            return False
        except requests.RequestException:
            print(f"{fw} BADS : {base} {fr}--> NO")
            return False

    def _write_result(self, url):
        with self._file_lock:
            with open(self.output_file, "a", encoding="utf-8") as f:
                f.write(url + "\n")

    def run(self, stop_on_first=False):
        """
        Run the scanner. If stop_on_first=True will stop after first vulnerable hit.
        """
        self._stop_on_first = bool(stop_on_first)
        if not self.sites:
            print(f"{fr}No sites loaded (file: {self.sites_file}). Exiting.")
            return

        tasks = []
        with ThreadPoolExecutor(max_workers=self.threads) as exe:
            future_to_target = {}
            for site in self.sites:
                for path in self.paths:
                    future = exe.submit(self._check_url, site, path)
                    future_to_target[future] = (site, path)

            try:
                for fut in as_completed(future_to_target):
                    try:
                        result = fut.result()
                        if result and self._stop_on_first:
                            # shutdown executor early
                            exe.shutdown(wait=False, cancel_futures=True)
                            break
                    except Exception as e:
                        site, path = future_to_target.get(fut, ("?", "?"))
                        print(f"{fr}Error checking {site}/{path}")
            except KeyboardInterrupt:
                print(f"{fr}Interrupted by user, shutting down.")

# For backwards compatibility & convenience
bads = h0rn3t
