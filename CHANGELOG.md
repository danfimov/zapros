# Changelog

## [0.9.0](https://github.com/danfimov/zapros/compare/v0.17.0...v0.9.0) (2026-09-02)


### ⚠ BREAKING CHANGES

* **models:** split Response.content into _source and _content
* deprecate `atext` and `ajson` helpers
* **types:** improve handler type annotations and deprecate misnamed middlewares

### Features

* add `ProxyMiddleware` ([495053e](https://github.com/danfimov/zapros/commit/495053ee43e3c3009cc861f36e8ec4a0c0c074e3))
* add ContentType header parsing and validation ([43984d5](https://github.com/danfimov/zapros/commit/43984d556ba334351ab86c35df4d356e23a7e11a))
* add mock call tracking helpers ([#27](https://github.com/danfimov/zapros/issues/27)) ([f86c588](https://github.com/danfimov/zapros/commit/f86c588f9858c6ed010d4274eec12b5d1fda7131))
* add Response.consumed flag ([6ff277b](https://github.com/danfimov/zapros/commit/6ff277b7a7a7d20f87e3e849e9fc4d9acbb9dc8c))
* add status class helpers on Response ([#36](https://github.com/danfimov/zapros/issues/36)) ([61a4f27](https://github.com/danfimov/zapros/commit/61a4f27409972c4d9c45e2b99e4ae6973e835c5d))
* add support for HTTP/2 ([#37](https://github.com/danfimov/zapros/issues/37)) ([5e7d47d](https://github.com/danfimov/zapros/commit/5e7d47d446c7eae187eec2a7a6fd9ac96ff5e5e1))
* add support for QUERY method ([ad50afa](https://github.com/danfimov/zapros/commit/ad50afa7e6f2d6870f69dafd08c1df9d85a024a8))
* add support for request trailing headers ([#46](https://github.com/danfimov/zapros/issues/46)) ([ce11928](https://github.com/danfimov/zapros/commit/ce11928a03f49b3073469c8a5c654a5c8258023c))
* add support for socks proxy ([550a483](https://github.com/danfimov/zapros/commit/550a483c8f2064fb7a4a2909f23bcf0b055acdf0))
* add support for trio ([e4c2469](https://github.com/danfimov/zapros/commit/e4c24692f0c2dcf4aa8ec64b440cc46cecb6f42d))
* add support for uvloop ([b1d55be](https://github.com/danfimov/zapros/commit/b1d55be42dab5ccd36904312047c7267e2a4edd7))
* add support for WebSockets ([#31](https://github.com/danfimov/zapros/issues/31)) ([ee25c6a](https://github.com/danfimov/zapros/commit/ee25c6a6cf6063fd7fcf73ead0cecf689091a19c))
* add URLSearchParams to public API ([739c2ac](https://github.com/danfimov/zapros/commit/739c2ac4f1754becb33140cd6a58fb366e9317b4))
* add ZaprosError ([e7ecaea](https://github.com/danfimov/zapros/commit/e7ecaeaa8d19be2527ea1cc513e942f42ff686af))
* allow extra items in request and response contextes ([339be31](https://github.com/danfimov/zapros/commit/339be316cb928d2e1b22edf206e44e2fb3f18af1))
* allow PathMatcher to match url using regex ([#29](https://github.com/danfimov/zapros/issues/29)) ([c61e454](https://github.com/danfimov/zapros/commit/c61e454b2862412393e7ddda73b0584e493f8dec))
* allow to set handler per-request ([b6919a6](https://github.com/danfimov/zapros/commit/b6919a6d6b60934d9cdc4b6ddb95ae0e08d4a100))
* **api:** add DNSResolutionError ([e88f282](https://github.com/danfimov/zapros/commit/e88f2824a0d61f26a8410004a7bbd1c2bed2286a))
* **api:** add SSLError ([6763281](https://github.com/danfimov/zapros/commit/6763281b1b40227e671435bc2a8008e3facf527c))
* **api:** add support for Response.raise_for_status ([a4f6784](https://github.com/danfimov/zapros/commit/a4f678447f645481352da0a7b97c90cb5ace730e))
* **asgi:** add Trio backend support to AsgiHandler ([1ed340f](https://github.com/danfimov/zapros/commit/1ed340f7e35770b719f85f27da74e876c9099f6d))
* better exceptions mapping ([79ecc9c](https://github.com/danfimov/zapros/commit/79ecc9cf0648dfc98c696f63eb9a5b6c1dbfb505))
* **client:** add base_url parameter for URL resolution ([2274816](https://github.com/danfimov/zapros/commit/2274816208a6966723bf34972a4571b2cc348fa4))
* expose `AsyncIOTransport` and `SyncTransport` classes ([0b6ef8a](https://github.com/danfimov/zapros/commit/0b6ef8aba4bf646694647afd045f9d1d070a25ea))
* expose request on Response ([cf00e82](https://github.com/danfimov/zapros/commit/cf00e829181f9d950b6eee1d6f751e9e4db04609))
* initial release ([35b7dc5](https://github.com/danfimov/zapros/commit/35b7dc5b931c1dbea788e1076652847543c31acb))
* **io:** add pluggable network transports ([408ddde](https://github.com/danfimov/zapros/commit/408dddeb30c509c19403fc49a15209df181319e8))
* **io:** properly handle TLS-in-TLS upgrades ([408ddde](https://github.com/danfimov/zapros/commit/408dddeb30c509c19403fc49a15209df181319e8))
* **perf:** use happy eyeballs by default in async handler ([793f2a2](https://github.com/danfimov/zapros/commit/793f2a277fc20c0199c1bb612942e5894b0c500c))
* raise StreamExhausted when reading exhausted response stream ([dfacd4f](https://github.com/danfimov/zapros/commit/dfacd4f39e2e350eb6e967c4dee65ab4b18cec71))
* replace unasync script with ry ([6761cd1](https://github.com/danfimov/zapros/commit/6761cd175160d95713de1436216fa2ed8e977c6d))
* **types:** allow None for Request's content-type arguments ([c7625fa](https://github.com/danfimov/zapros/commit/c7625fa2a08ba91217419ae9e08fc251eea8e19b))


### Bug Fixes

* **asyncio:** await transport teardown on stream close ([2c40db3](https://github.com/danfimov/zapros/commit/2c40db36557e830fb79d6a30002f5cfb9832b26d))
* **caching:** properly handle cases when body was consumed before reaching cache ([d68cbc0](https://github.com/danfimov/zapros/commit/d68cbc0c58f63e5121fb47ef4e8ac8e248ffd898))
* do not buffer the response data in `iter_bytes` ([ef93fd1](https://github.com/danfimov/zapros/commit/ef93fd19229cf8268cdded23eaa23a4b4018c1a9))
* do not try to import pyreqwest on python3.10 ([fb968d7](https://github.com/danfimov/zapros/commit/fb968d71a558938b528f3d8081f5205a3f881bca))
* **docs:** update the hishel references ([f840441](https://github.com/danfimov/zapros/commit/f8404412c9aef2d0e1e72f6a0fe3a05a05f349a6))
* drop unnecessary Headers object creations inside connection_wants_close ([#48](https://github.com/danfimov/zapros/issues/48)) ([86becc2](https://github.com/danfimov/zapros/commit/86becc20e1e7ec879116b8c40ba1aefc4af0208d))
* ensure Response.aclose/close properly releases stream resources ([4d08138](https://github.com/danfimov/zapros/commit/4d081383e23ca6de4ddc8d8fbf0fd37eb0f9373b))
* fix support for python3.10 ([0205dd1](https://github.com/danfimov/zapros/commit/0205dd1b4d81444e5671a56bed503025a1334d12))
* **handlers:** handle 101 websocket upgrade responses ([035eb2e](https://github.com/danfimov/zapros/commit/035eb2eae3e18cef4f00b322448c6801077e41a4))
* make connection pooling proxy-aware ([3c64504](https://github.com/danfimov/zapros/commit/3c64504b7369f2cf9e682815f1ae99de20f88034))
* make mypy happy with base handler shape ([6490251](https://github.com/danfimov/zapros/commit/6490251e4aaf674cf44ff76bc7c7b7eee06cf476))
* **pool:** narrow down some broad type catches ([db5cb6c](https://github.com/danfimov/zapros/commit/db5cb6c02ecb0513747be1afa273b286619f186c))
* **proxies:** respect credentials in the proxy url ([5852aa6](https://github.com/danfimov/zapros/commit/5852aa611887158a4284d5c65185e1c73d7e403e))
* **pyodide:** strip out content-encoding header as fetch always decompresses ([14ef378](https://github.com/danfimov/zapros/commit/14ef378cefa38a65207bcb6e0d9c725fb494f86d))
* remove body-related arguments from get and head methods ([37fc100](https://github.com/danfimov/zapros/commit/37fc100c020df6b36cc5334dc11b8ec54ec3a82c))
* return usable handoff transport for 101 responses ([78a0a1e](https://github.com/danfimov/zapros/commit/78a0a1e5096995f007a7454528b1ced15ed7aba0))
* **security:** limit Content-Encoding layers to 5 ([7971fbc](https://github.com/danfimov/zapros/commit/7971fbca9707eb01455ca2d73416ac091f96908b))
* **security:** protect streaming responses from zip bombs ([9b59fa6](https://github.com/danfimov/zapros/commit/9b59fa65857734599c34b0b3dff4c2b62293a68d))
* ssl_handshake_timeout is only meaningful with ssl ([#34](https://github.com/danfimov/zapros/issues/34)) ([f35c63b](https://github.com/danfimov/zapros/commit/f35c63bfbe3975ebee3b2de7cbf51a3bb1ffc1d0))
* **types:** correct `next_handler` type annotations in handlers ([f174810](https://github.com/danfimov/zapros/commit/f17481082522d8276d5969d753fd9b631a112f55))
* **types:** improve handler type annotations and deprecate misnamed middlewares ([2376086](https://github.com/danfimov/zapros/commit/2376086b4e4c385cbb9f970d8d3853ca189a353a))


### Chores

* add CI test for pyodide support ([3c03a8f](https://github.com/danfimov/zapros/commit/3c03a8f4200f57e25cd36c2898fe523e1bf0766d))
* add parser for Connection header ([367e402](https://github.com/danfimov/zapros/commit/367e40230252435d36b126e22ff845a294af260d))
* add py.typed file ([ee7ed8a](https://github.com/danfimov/zapros/commit/ee7ed8a7e5453f2d898347f46e607d27d0590015))
* **ai:** add an agent skill + claude plugin ([e5dbcc2](https://github.com/danfimov/zapros/commit/e5dbcc2af40cbeca5dddafe99420ecba8d8989ba))
* bump ry version, get rid of bunch of ids ([5c166f8](https://github.com/danfimov/zapros/commit/5c166f8b50bf8261469e7b9cfe253e1401a89837))
* bump ry version, simplify ry.yml ([ed05152](https://github.com/danfimov/zapros/commit/ed051528aae87dcb1384a027caf8b9bf7787f6cb))
* bump ry version, tidy up tests ([311871f](https://github.com/danfimov/zapros/commit/311871f3bc5832f27898d0f258dda87dc4190172))
* disable release-please prerelease mode ([7fe0f3a](https://github.com/danfimov/zapros/commit/7fe0f3aea51a25940c51b07dd312aac9283afa55))
* do not echo host port in the mock server ([24dae9f](https://github.com/danfimov/zapros/commit/24dae9f6d9993198383175f5673cbf084652fff4))
* explicitly set build-system in pyproject.toml ([aaa6e56](https://github.com/danfimov/zapros/commit/aaa6e56b6949db08c31a1ccb891952ed136c26ed))
* fix logo link in the README ([2c05bb0](https://github.com/danfimov/zapros/commit/2c05bb0190eadca0dfae10835b2efabe956246f6))
* fix release-config path ([dcc39ba](https://github.com/danfimov/zapros/commit/dcc39ba8580ef613e175552ce8754bfae173133a))
* fix the spider’s leg count :D ([833e94b](https://github.com/danfimov/zapros/commit/833e94b94b22cfeaa11a0ddd5f4ce42a36d9bc29))
* generate more sync code ([ef19b40](https://github.com/danfimov/zapros/commit/ef19b40741975c954457b96e8264d1f371754255))
* **main:** release 0.10.0 ([#25](https://github.com/danfimov/zapros/issues/25)) ([82fbde2](https://github.com/danfimov/zapros/commit/82fbde258a98e6e42c07b26817aa55e218ecb751))
* **main:** release 0.11.0 ([#30](https://github.com/danfimov/zapros/issues/30)) ([1f8e341](https://github.com/danfimov/zapros/commit/1f8e3417d133dde7808a722c1abe01cee47d3dfc))
* **main:** release 0.11.1 ([#32](https://github.com/danfimov/zapros/issues/32)) ([160acf5](https://github.com/danfimov/zapros/commit/160acf5900d77176b26b56c84176443c97fa2dbe))
* **main:** release 0.12.0 ([#35](https://github.com/danfimov/zapros/issues/35)) ([d20c204](https://github.com/danfimov/zapros/commit/d20c204529e01ad6a20fe31a63962e8c203903d4))
* **main:** release 0.13.0 ([#38](https://github.com/danfimov/zapros/issues/38)) ([4c9b779](https://github.com/danfimov/zapros/commit/4c9b7794a92fc15bc31c6989937c4f86996b6625))
* **main:** release 0.14.0 ([#39](https://github.com/danfimov/zapros/issues/39)) ([ac1510f](https://github.com/danfimov/zapros/commit/ac1510f14665db5dcd806931f5511c8e5ac3ef63))
* **main:** release 0.15.0 ([#40](https://github.com/danfimov/zapros/issues/40)) ([b15174a](https://github.com/danfimov/zapros/commit/b15174a6c543e06faf6658875916ad644aa734c8))
* **main:** release 0.16.0 ([#41](https://github.com/danfimov/zapros/issues/41)) ([8733e89](https://github.com/danfimov/zapros/commit/8733e8954b464743546942437e7a59e53a800793))
* **main:** release 0.17.0 ([#42](https://github.com/danfimov/zapros/issues/42)) ([8a0c5de](https://github.com/danfimov/zapros/commit/8a0c5dee3dbfb2a8b1d999ec5831413c8163fd2b))
* **main:** release 0.2.0 ([#1](https://github.com/danfimov/zapros/issues/1)) ([e1eedd4](https://github.com/danfimov/zapros/commit/e1eedd41b8d2c9bdb3014882cb2a6b4d1cc0528a))
* **main:** release 0.6.0 ([#17](https://github.com/danfimov/zapros/issues/17)) ([76a556d](https://github.com/danfimov/zapros/commit/76a556d280e4e09a6fafa66b5a11b7f24953c10a))
* **main:** release 0.7.0 ([#18](https://github.com/danfimov/zapros/issues/18)) ([b13c95a](https://github.com/danfimov/zapros/commit/b13c95a30e1787fce44e5143fba2417a6bd39a18))
* **main:** release 0.8.0 ([#20](https://github.com/danfimov/zapros/issues/20)) ([d28b6d3](https://github.com/danfimov/zapros/commit/d28b6d38af5818213a3f34c3f549f9662adaf60d))
* **main:** release 0.9.0 ([#21](https://github.com/danfimov/zapros/issues/21)) ([0da6a98](https://github.com/danfimov/zapros/commit/0da6a98d4ad274735cdcf4098a0ddf872e62ec33))
* **main:** release zapros 0.2.1 ([#2](https://github.com/danfimov/zapros/issues/2)) ([1594757](https://github.com/danfimov/zapros/commit/15947579ba527981078d2e95c0df6928741732b3))
* **main:** release zapros 0.2.2 ([#3](https://github.com/danfimov/zapros/issues/3)) ([26437a6](https://github.com/danfimov/zapros/commit/26437a6ef07a1e733c5fde7fa360c8ecdd10d34d))
* **main:** release zapros 0.2.3 ([#4](https://github.com/danfimov/zapros/issues/4)) ([f5dd41e](https://github.com/danfimov/zapros/commit/f5dd41ec376b0e871b959991c1a5d57cde1825f0))
* **main:** release zapros 0.3.0 ([#5](https://github.com/danfimov/zapros/issues/5)) ([9b4a7c6](https://github.com/danfimov/zapros/commit/9b4a7c6952639f6ef73fe14cf47a282f7db07ad1))
* **main:** release zapros 0.4.0 ([#8](https://github.com/danfimov/zapros/issues/8)) ([4cd293a](https://github.com/danfimov/zapros/commit/4cd293a37791124052f83f8c845593bb47a74372))
* **main:** release zapros 0.5.0 ([#12](https://github.com/danfimov/zapros/issues/12)) ([926ee4b](https://github.com/danfimov/zapros/commit/926ee4bdced8b2f10ace3125359bc7aa9515cd52))
* **main:** release zapros 0.5.1 ([#13](https://github.com/danfimov/zapros/issues/13)) ([ffdde67](https://github.com/danfimov/zapros/commit/ffdde67b9a2dac5e3df5a932cc53a63ae911ffca))
* make test script to pass additional arguments to pytest ([83f1c10](https://github.com/danfimov/zapros/commit/83f1c10598248834b3bd9e58fa1f7e9f3c92a278))
* release 0.3.0 ([9eae1b3](https://github.com/danfimov/zapros/commit/9eae1b372b0e7a42474b1fb6fcec41babd7b2242))
* release 0.8.0 ([3966f38](https://github.com/danfimov/zapros/commit/3966f38ec6924fdbd1ddd4d63d5953c324f0333b))
* remove .python-version ([889df55](https://github.com/danfimov/zapros/commit/889df5504d483f0666ddea11d9435e6aabe1969d))
* remove duplicated release-please config ([0105c9c](https://github.com/danfimov/zapros/commit/0105c9c227365de7d4a36c1ce776548592e7fe7f))
* update uv.lock ([daff37b](https://github.com/danfimov/zapros/commit/daff37beea572337b930d793f03e7733b0b5e6fa))
* update uv.lock ([7982c50](https://github.com/danfimov/zapros/commit/7982c508b4d3ec46e73549650fd5d09cbe786f16))
* use always-bump versioning ([1155098](https://github.com/danfimov/zapros/commit/11550987c9a37d371df702ea9e436bf98cde9ff1))
* very simple commit ([d00db56](https://github.com/danfimov/zapros/commit/d00db562b8a2b252bddcffcb7ba40ae9d44ed998))


### Documentation

* add async/sync separation guide with error links ([6841ef6](https://github.com/danfimov/zapros/commit/6841ef6e4c6e76813799365bb3c7a50f8ebfaff5))
* add basic benchmark example ([89e711f](https://github.com/danfimov/zapros/commit/89e711fb6c905accdd2d62c50a0aadab63f5c876))
* add docs for proxies ([5852aa6](https://github.com/danfimov/zapros/commit/5852aa611887158a4284d5c65185e1c73d7e403e))
* add docs for std handlers ([eac0ca1](https://github.com/danfimov/zapros/commit/eac0ca1ccea26d17967626ef21e85065e9ff59fc))
* add missing sync examples in websocket page ([a657026](https://github.com/danfimov/zapros/commit/a657026f0aeea5b485a76eb1191d4190f9a931fe))
* add OAuth authorization code flow example ([e286ec9](https://github.com/danfimov/zapros/commit/e286ec9d3466cef716432f4dce15b3b49d8147e8))
* add pronunciation guide ([553a812](https://github.com/danfimov/zapros/commit/553a812407e653b868900d900adc13a2dd0b59db))
* document how to use zapros in browser ([c5ee3dc](https://github.com/danfimov/zapros/commit/c5ee3dcb1943ae7df7f0ff54cca2bb321999ef08))
* fix caching feature name ([a575bbe](https://github.com/danfimov/zapros/commit/a575bbe0e286975c3ce17162f4c9e34cc18c4045))
* fix the browser example, use CORS-free endpoint ([1f9e0ab](https://github.com/danfimov/zapros/commit/1f9e0ab97eafaf12f8e1a95d005abddc5a86513d))
* fix the github link ([896d993](https://github.com/danfimov/zapros/commit/896d993eac8cae667bd82dc71b3a151681f06cc2))
* fix typo in cassettes page ([4d086bc](https://github.com/danfimov/zapros/commit/4d086bcbe574947ba74f6c9daae7637404d5ceaf))
* Improve wording of what `mock_http` patches ([#26](https://github.com/danfimov/zapros/issues/26)) ([fab280c](https://github.com/danfimov/zapros/commit/fab280ccd58a38e420989f5b6ce7dcd1bc005484))
* mock_http should be used as sync context manager ([#23](https://github.com/danfimov/zapros/issues/23)) ([fd3063c](https://github.com/danfimov/zapros/commit/fd3063c6c1f5b42f401cd31dad57f1f18092e75b))
* remove redundant doc files ([e4c4885](https://github.com/danfimov/zapros/commit/e4c4885c5c1e176b302c31b5b16d3f40494ea7ad))
* remove the newborn part from the readme ([6a73dc9](https://github.com/danfimov/zapros/commit/6a73dc9788ae99b12fb30cbf5867145f36a240b2))
* separate matchers documentation ([6065c3b](https://github.com/danfimov/zapros/commit/6065c3bad47b1bef3fbacbf48c6b737c34f2ebac))
* suggest avoiding ([2b67277](https://github.com/danfimov/zapros/commit/2b6727722b23ac69707866cd36fc7dfab1b5ea34))
* use router.add instead of Mock.mount for better formatting ([34c54e4](https://github.com/danfimov/zapros/commit/34c54e4a069e6bbfe2eb9773997c526f40f2e57b))


### Refactors

* **cassettes:** deprecate Cassette, move some arguments to CassetteMiddleware ([a2e4eeb](https://github.com/danfimov/zapros/commit/a2e4eeb9bdad964813c49e85de693ea26f4e3c40))
* deprecate `atext` and `ajson` helpers ([0ed8d08](https://github.com/danfimov/zapros/commit/0ed8d08a1a2ce78434778d9f05fd9edec32bcf6c))
* **handlers:** abstract connections from std handlers ([a29f728](https://github.com/danfimov/zapros/commit/a29f72828e807e7dbb09380e1f1d3040780fa0a5))
* **handlers:** consolidate timeout helpers in _common ([f62ff18](https://github.com/danfimov/zapros/commit/f62ff18655d4e28332eefb555a8b96231db0725e))
* **handlers:** deduplicate the broken connection error ([a7e0d6c](https://github.com/danfimov/zapros/commit/a7e0d6ca7897140060398d98d9ee79a26d9e4b1f))
* **handlers:** streamline HTTP request-line target construction ([88238dd](https://github.com/danfimov/zapros/commit/88238dd84d057eafacb7b9f318cee9e985e3f1dd))
* **internal:** rename _source to _content ([1793b9b](https://github.com/danfimov/zapros/commit/1793b9bb3a4fbb423f8324ec8a48603dda9500f2))
* **models:** split Response.content into _source and _content ([be45aea](https://github.com/danfimov/zapros/commit/be45aead4f2c8482b4d36a9227959e5d7ea3774c))
* simplify asgi handler by buffering the bodies ([b84e1e1](https://github.com/danfimov/zapros/commit/b84e1e1067a7b6fec156333d51cc1a771843d458))
* simplify cassette url normalizer ([1f0a304](https://github.com/danfimov/zapros/commit/1f0a30403629a000b15d2b7472a044ab3b732165))
* simplify zapros to hishel conversion ([62e9f83](https://github.com/danfimov/zapros/commit/62e9f83e74f857c1d74d7af3a0e87f018f69cf25))
* unify sync and async connection pool interfaces ([c8778bb](https://github.com/danfimov/zapros/commit/c8778bba570ff780c8a5c4664ca5bc9ffe1fd457))

## [0.17.0](https://github.com/kap-sh/zapros/compare/v0.16.0...v0.17.0) (2026-08-26)


### Features

* add support for request trailing headers ([#46](https://github.com/kap-sh/zapros/issues/46)) ([ce11928](https://github.com/kap-sh/zapros/commit/ce11928a03f49b3073469c8a5c654a5c8258023c))


### Documentation

* remove redundant doc files ([e4c4885](https://github.com/kap-sh/zapros/commit/e4c4885c5c1e176b302c31b5b16d3f40494ea7ad))
* remove the newborn part from the readme ([6a73dc9](https://github.com/kap-sh/zapros/commit/6a73dc9788ae99b12fb30cbf5867145f36a240b2))

## [0.16.0](https://github.com/kap-sh/zapros/compare/v0.15.0...v0.16.0) (2026-07-04)


### Bug Fixes

* **asyncio:** await transport teardown on stream close ([2c40db3](https://github.com/kap-sh/zapros/commit/2c40db36557e830fb79d6a30002f5cfb9832b26d))

## [0.15.0](https://github.com/kap-sh/zapros/compare/v0.14.0...v0.15.0) (2026-06-24)


### Features

* add support for QUERY method ([ad50afa](https://github.com/kap-sh/zapros/commit/ad50afa7e6f2d6870f69dafd08c1df9d85a024a8))
* allow to set handler per-request ([b6919a6](https://github.com/kap-sh/zapros/commit/b6919a6d6b60934d9cdc4b6ddb95ae0e08d4a100))

## [0.14.0](https://github.com/kap-sh/zapros/compare/v0.13.0...v0.14.0) (2026-06-23)


### Bug Fixes

* **security:** limit Content-Encoding layers to 5 ([7971fbc](https://github.com/kap-sh/zapros/commit/7971fbca9707eb01455ca2d73416ac091f96908b))
* **security:** protect streaming responses from zip bombs ([9b59fa6](https://github.com/kap-sh/zapros/commit/9b59fa65857734599c34b0b3dff4c2b62293a68d))

## [0.13.0](https://github.com/kap-sh/zapros/compare/v0.12.0...v0.13.0) (2026-06-06)


### Features

* allow extra items in request and response contextes ([339be31](https://github.com/kap-sh/zapros/commit/339be316cb928d2e1b22edf206e44e2fb3f18af1))
* **types:** allow None for Request's content-type arguments ([c7625fa](https://github.com/kap-sh/zapros/commit/c7625fa2a08ba91217419ae9e08fc251eea8e19b))

## [0.12.0](https://github.com/kap-sh/zapros/compare/v0.11.1...v0.12.0) (2026-05-19)


### Features

* add status class helpers on Response ([#36](https://github.com/kap-sh/zapros/issues/36)) ([61a4f27](https://github.com/kap-sh/zapros/commit/61a4f27409972c4d9c45e2b99e4ae6973e835c5d))
* add support for HTTP/2 ([#37](https://github.com/kap-sh/zapros/issues/37)) ([5e7d47d](https://github.com/kap-sh/zapros/commit/5e7d47d446c7eae187eec2a7a6fd9ac96ff5e5e1))
* expose request on Response ([cf00e82](https://github.com/kap-sh/zapros/commit/cf00e829181f9d950b6eee1d6f751e9e4db04609))
* raise StreamExhausted when reading exhausted response stream ([dfacd4f](https://github.com/kap-sh/zapros/commit/dfacd4f39e2e350eb6e967c4dee65ab4b18cec71))


### Bug Fixes

* **docs:** update the hishel references ([f840441](https://github.com/kap-sh/zapros/commit/f8404412c9aef2d0e1e72f6a0fe3a05a05f349a6))


### Chores

* make test script to pass additional arguments to pytest ([83f1c10](https://github.com/kap-sh/zapros/commit/83f1c10598248834b3bd9e58fa1f7e9f3c92a278))


### Documentation

* add pronunciation guide ([553a812](https://github.com/kap-sh/zapros/commit/553a812407e653b868900d900adc13a2dd0b59db))
* use router.add instead of Mock.mount for better formatting ([34c54e4](https://github.com/kap-sh/zapros/commit/34c54e4a069e6bbfe2eb9773997c526f40f2e57b))


### Refactors

* **handlers:** abstract connections from std handlers ([a29f728](https://github.com/kap-sh/zapros/commit/a29f72828e807e7dbb09380e1f1d3040780fa0a5))
* **handlers:** consolidate timeout helpers in _common ([f62ff18](https://github.com/kap-sh/zapros/commit/f62ff18655d4e28332eefb555a8b96231db0725e))
* **handlers:** deduplicate the broken connection error ([a7e0d6c](https://github.com/kap-sh/zapros/commit/a7e0d6ca7897140060398d98d9ee79a26d9e4b1f))
* **handlers:** streamline HTTP request-line target construction ([88238dd](https://github.com/kap-sh/zapros/commit/88238dd84d057eafacb7b9f318cee9e985e3f1dd))

## [0.11.1](https://github.com/kap-sh/zapros/compare/v0.11.0...v0.11.1) (2026-05-05)


### Bug Fixes

* ssl_handshake_timeout is only meaningful with ssl ([#34](https://github.com/kap-sh/zapros/issues/34)) ([f35c63b](https://github.com/kap-sh/zapros/commit/f35c63bfbe3975ebee3b2de7cbf51a3bb1ffc1d0))


### Documentation

* add missing sync examples in websocket page ([a657026](https://github.com/kap-sh/zapros/commit/a657026f0aeea5b485a76eb1191d4190f9a931fe))

## [0.11.0](https://github.com/kap-sh/zapros/compare/v0.10.0...v0.11.0) (2026-05-05)


### Features

* add support for uvloop ([b1d55be](https://github.com/kap-sh/zapros/commit/b1d55be42dab5ccd36904312047c7267e2a4edd7))
* add support for WebSockets ([#31](https://github.com/kap-sh/zapros/issues/31)) ([ee25c6a](https://github.com/kap-sh/zapros/commit/ee25c6a6cf6063fd7fcf73ead0cecf689091a19c))
* allow PathMatcher to match url using regex ([#29](https://github.com/kap-sh/zapros/issues/29)) ([c61e454](https://github.com/kap-sh/zapros/commit/c61e454b2862412393e7ddda73b0584e493f8dec))
* **asgi:** add Trio backend support to AsgiHandler ([1ed340f](https://github.com/kap-sh/zapros/commit/1ed340f7e35770b719f85f27da74e876c9099f6d))


### Chores

* add parser for Connection header ([367e402](https://github.com/kap-sh/zapros/commit/367e40230252435d36b126e22ff845a294af260d))
* explicitly set build-system in pyproject.toml ([aaa6e56](https://github.com/kap-sh/zapros/commit/aaa6e56b6949db08c31a1ccb891952ed136c26ed))


### Refactors

* simplify asgi handler by buffering the bodies ([b84e1e1](https://github.com/kap-sh/zapros/commit/b84e1e1067a7b6fec156333d51cc1a771843d458))

## [0.10.0](https://github.com/kap-sh/zapros/compare/v0.9.0...v0.10.0) (2026-04-27)


### Features

* add mock call tracking helpers ([#27](https://github.com/kap-sh/zapros/issues/27)) ([f86c588](https://github.com/kap-sh/zapros/commit/f86c588f9858c6ed010d4274eec12b5d1fda7131))
* **client:** add base_url parameter for URL resolution ([2274816](https://github.com/kap-sh/zapros/commit/2274816208a6966723bf34972a4571b2cc348fa4))


### Bug Fixes

* make mypy happy with base handler shape ([6490251](https://github.com/kap-sh/zapros/commit/6490251e4aaf674cf44ff76bc7c7b7eee06cf476))


### Documentation

* Improve wording of what `mock_http` patches ([#26](https://github.com/kap-sh/zapros/issues/26)) ([fab280c](https://github.com/kap-sh/zapros/commit/fab280ccd58a38e420989f5b6ce7dcd1bc005484))
* mock_http should be used as sync context manager ([#23](https://github.com/kap-sh/zapros/issues/23)) ([fd3063c](https://github.com/kap-sh/zapros/commit/fd3063c6c1f5b42f401cd31dad57f1f18092e75b))
* separate matchers documentation ([6065c3b](https://github.com/kap-sh/zapros/commit/6065c3bad47b1bef3fbacbf48c6b737c34f2ebac))
* suggest avoiding ([2b67277](https://github.com/kap-sh/zapros/commit/2b6727722b23ac69707866cd36fc7dfab1b5ea34))

## [0.9.0](https://github.com/kap-sh/zapros/compare/v0.8.0...v0.9.0) (2026-04-24)


### Bug Fixes

* **pyodide:** strip out content-encoding header as fetch always decompresses ([14ef378](https://github.com/kap-sh/zapros/commit/14ef378cefa38a65207bcb6e0d9c725fb494f86d))


### Documentation

* fix the browser example, use CORS-free endpoint ([1f9e0ab](https://github.com/kap-sh/zapros/commit/1f9e0ab97eafaf12f8e1a95d005abddc5a86513d))

## [0.8.0](https://github.com/kap-sh/zapros/compare/v0.7.0...v0.8.0) (2026-04-24)


### Chores

* add CI test for pyodide support ([3c03a8f](https://github.com/kap-sh/zapros/commit/3c03a8f4200f57e25cd36c2898fe523e1bf0766d))
* release 0.8.0 ([3966f38](https://github.com/kap-sh/zapros/commit/3966f38ec6924fdbd1ddd4d63d5953c324f0333b))


### Documentation

* document how to use zapros in browser ([c5ee3dc](https://github.com/kap-sh/zapros/commit/c5ee3dcb1943ae7df7f0ff54cca2bb321999ef08))

## [0.7.0](https://github.com/kap-sh/zapros/compare/v0.6.0...v0.7.0) (2026-04-19)


### ⚠ BREAKING CHANGES

* **models:** split Response.content into _source and _content

### Features

* add ContentType header parsing and validation ([43984d5](https://github.com/kap-sh/zapros/commit/43984d556ba334351ab86c35df4d356e23a7e11a))
* add Response.consumed flag ([6ff277b](https://github.com/kap-sh/zapros/commit/6ff277b7a7a7d20f87e3e849e9fc4d9acbb9dc8c))


### Bug Fixes

* **caching:** properly handle cases when body was consumed before reaching cache ([d68cbc0](https://github.com/kap-sh/zapros/commit/d68cbc0c58f63e5121fb47ef4e8ac8e248ffd898))


### Chores

* bump ry version, simplify ry.yml ([ed05152](https://github.com/kap-sh/zapros/commit/ed051528aae87dcb1384a027caf8b9bf7787f6cb))
* disable release-please prerelease mode ([7fe0f3a](https://github.com/kap-sh/zapros/commit/7fe0f3aea51a25940c51b07dd312aac9283afa55))
* generate more sync code ([ef19b40](https://github.com/kap-sh/zapros/commit/ef19b40741975c954457b96e8264d1f371754255))


### Documentation

* fix typo in cassettes page ([4d086bc](https://github.com/kap-sh/zapros/commit/4d086bcbe574947ba74f6c9daae7637404d5ceaf))


### Refactors

* **cassettes:** deprecate Cassette, move some arguments to CassetteMiddleware ([a2e4eeb](https://github.com/kap-sh/zapros/commit/a2e4eeb9bdad964813c49e85de693ea26f4e3c40))
* **internal:** rename _source to _content ([1793b9b](https://github.com/kap-sh/zapros/commit/1793b9bb3a4fbb423f8324ec8a48603dda9500f2))
* **models:** split Response.content into _source and _content ([be45aea](https://github.com/kap-sh/zapros/commit/be45aead4f2c8482b4d36a9227959e5d7ea3774c))
* simplify cassette url normalizer ([1f0a304](https://github.com/kap-sh/zapros/commit/1f0a30403629a000b15d2b7472a044ab3b732165))
* simplify zapros to hishel conversion ([62e9f83](https://github.com/kap-sh/zapros/commit/62e9f83e74f857c1d74d7af3a0e87f018f69cf25))

## [0.6.0](https://github.com/kap-sh/zapros/compare/v0.5.1...v0.6.0) (2026-04-12)


### Features

* add support for trio ([e4c2469](https://github.com/kap-sh/zapros/commit/e4c24692f0c2dcf4aa8ec64b440cc46cecb6f42d))
* better exceptions mapping ([79ecc9c](https://github.com/kap-sh/zapros/commit/79ecc9cf0648dfc98c696f63eb9a5b6c1dbfb505))


### Chores

* bump ry version, get rid of bunch of ids ([5c166f8](https://github.com/kap-sh/zapros/commit/5c166f8b50bf8261469e7b9cfe253e1401a89837))
* bump ry version, tidy up tests ([311871f](https://github.com/kap-sh/zapros/commit/311871f3bc5832f27898d0f258dda87dc4190172))
* update uv.lock ([daff37b](https://github.com/kap-sh/zapros/commit/daff37beea572337b930d793f03e7733b0b5e6fa))

## [0.5.1](https://github.com/kap-sh/zapros/compare/zapros-v0.5.0...zapros-v0.5.1) (2026-04-08)


### Features

* add support for socks proxy ([550a483](https://github.com/kap-sh/zapros/commit/550a483c8f2064fb7a4a2909f23bcf0b055acdf0))
* **api:** add DNSResolutionError ([e88f282](https://github.com/kap-sh/zapros/commit/e88f2824a0d61f26a8410004a7bbd1c2bed2286a))
* **api:** add SSLError ([6763281](https://github.com/kap-sh/zapros/commit/6763281b1b40227e671435bc2a8008e3facf527c))
* **api:** add support for Response.raise_for_status ([a4f6784](https://github.com/kap-sh/zapros/commit/a4f678447f645481352da0a7b97c90cb5ace730e))
* replace unasync script with ry ([6761cd1](https://github.com/kap-sh/zapros/commit/6761cd175160d95713de1436216fa2ed8e977c6d))


### Bug Fixes

* do not buffer the response data in `iter_bytes` ([ef93fd1](https://github.com/kap-sh/zapros/commit/ef93fd19229cf8268cdded23eaa23a4b4018c1a9))

## [0.5.0](https://github.com/kap-sh/zapros/compare/zapros-v0.4.0...zapros-v0.5.0) (2026-04-04)


### ⚠ BREAKING CHANGES

* deprecate `atext` and `ajson` helpers

### Features

* add ZaprosError ([e7ecaea](https://github.com/kap-sh/zapros/commit/e7ecaeaa8d19be2527ea1cc513e942f42ff686af))
* expose `AsyncIOTransport` and `SyncTransport` classes ([0b6ef8a](https://github.com/kap-sh/zapros/commit/0b6ef8aba4bf646694647afd045f9d1d070a25ea))


### Documentation

* add docs for std handlers ([eac0ca1](https://github.com/kap-sh/zapros/commit/eac0ca1ccea26d17967626ef21e85065e9ff59fc))


### Code Refactoring

* deprecate `atext` and `ajson` helpers ([0ed8d08](https://github.com/kap-sh/zapros/commit/0ed8d08a1a2ce78434778d9f05fd9edec32bcf6c))

## [0.4.0](https://github.com/kap-sh/zapros/compare/zapros-v0.3.0...zapros-v0.4.0) (2026-04-04)


### ⚠ BREAKING CHANGES

* **types:** improve handler type annotations and deprecate misnamed middlewares

### Features

* add `ProxyMiddleware` ([495053e](https://github.com/kap-sh/zapros/commit/495053ee43e3c3009cc861f36e8ec4a0c0c074e3))
* **io:** add pluggable network transports ([408ddde](https://github.com/kap-sh/zapros/commit/408dddeb30c509c19403fc49a15209df181319e8))
* **io:** properly handle TLS-in-TLS upgrades ([408ddde](https://github.com/kap-sh/zapros/commit/408dddeb30c509c19403fc49a15209df181319e8))


### Bug Fixes

* **handlers:** handle 101 websocket upgrade responses ([035eb2e](https://github.com/kap-sh/zapros/commit/035eb2eae3e18cef4f00b322448c6801077e41a4))
* make connection pooling proxy-aware ([3c64504](https://github.com/kap-sh/zapros/commit/3c64504b7369f2cf9e682815f1ae99de20f88034))
* **pool:** narrow down some broad type catches ([db5cb6c](https://github.com/kap-sh/zapros/commit/db5cb6c02ecb0513747be1afa273b286619f186c))
* **proxies:** respect credentials in the proxy url ([5852aa6](https://github.com/kap-sh/zapros/commit/5852aa611887158a4284d5c65185e1c73d7e403e))
* remove body-related arguments from get and head methods ([37fc100](https://github.com/kap-sh/zapros/commit/37fc100c020df6b36cc5334dc11b8ec54ec3a82c))
* return usable handoff transport for 101 responses ([78a0a1e](https://github.com/kap-sh/zapros/commit/78a0a1e5096995f007a7454528b1ced15ed7aba0))
* **types:** correct `next_handler` type annotations in handlers ([f174810](https://github.com/kap-sh/zapros/commit/f17481082522d8276d5969d753fd9b631a112f55))
* **types:** improve handler type annotations and deprecate misnamed middlewares ([2376086](https://github.com/kap-sh/zapros/commit/2376086b4e4c385cbb9f970d8d3853ca189a353a))


### Documentation

* add docs for proxies ([5852aa6](https://github.com/kap-sh/zapros/commit/5852aa611887158a4284d5c65185e1c73d7e403e))

## [0.3.0](https://github.com/kap-sh/zapros/compare/zapros-v0.2.3...zapros-v0.3.0) (2026-03-21)


### Features

* add URLSearchParams to public API ([739c2ac](https://github.com/kap-sh/zapros/commit/739c2ac4f1754becb33140cd6a58fb366e9317b4))
* **perf:** use happy eyeballs by default in async handler ([793f2a2](https://github.com/kap-sh/zapros/commit/793f2a277fc20c0199c1bb612942e5894b0c500c))


### Bug Fixes

* ensure Response.aclose/close properly releases stream resources ([4d08138](https://github.com/kap-sh/zapros/commit/4d081383e23ca6de4ddc8d8fbf0fd37eb0f9373b))


### Documentation

* add async/sync separation guide with error links ([6841ef6](https://github.com/kap-sh/zapros/commit/6841ef6e4c6e76813799365bb3c7a50f8ebfaff5))
* add basic benchmark example ([89e711f](https://github.com/kap-sh/zapros/commit/89e711fb6c905accdd2d62c50a0aadab63f5c876))
* add OAuth authorization code flow example ([e286ec9](https://github.com/kap-sh/zapros/commit/e286ec9d3466cef716432f4dce15b3b49d8147e8))
* fix caching feature name ([a575bbe](https://github.com/kap-sh/zapros/commit/a575bbe0e286975c3ce17162f4c9e34cc18c4045))


### Miscellaneous Chores

* release 0.3.0 ([9eae1b3](https://github.com/kap-sh/zapros/commit/9eae1b372b0e7a42474b1fb6fcec41babd7b2242))

## [0.2.3](https://github.com/kap-sh/zapros/compare/zapros-v0.2.2...zapros-v0.2.3) (2026-03-14)


### Bug Fixes

* do not try to import pyreqwest on python3.10 ([fb968d7](https://github.com/kap-sh/zapros/commit/fb968d71a558938b528f3d8081f5205a3f881bca))
* fix support for python3.10 ([0205dd1](https://github.com/kap-sh/zapros/commit/0205dd1b4d81444e5671a56bed503025a1334d12))

## [0.2.2](https://github.com/kap-sh/zapros/compare/zapros-v0.2.1...zapros-v0.2.2) (2026-03-14)


### Documentation

* fix the github link ([896d993](https://github.com/kap-sh/zapros/commit/896d993eac8cae667bd82dc71b3a151681f06cc2))

## [0.2.1](https://github.com/kap-sh/zapros/compare/zapros-v0.2.0...zapros-v0.2.1) (2026-03-14)


### Features

* initial release ([35b7dc5](https://github.com/kap-sh/zapros/commit/35b7dc5b931c1dbea788e1076652847543c31acb))

## [0.2.0](https://github.com/kap-sh/zapros/compare/v0.1.1...v0.2.0) (2026-03-14)


### Features

* initial release ([35b7dc5](https://github.com/kap-sh/zapros/commit/35b7dc5b931c1dbea788e1076652847543c31acb))

## 0.1.0 (2026-03-13)


### Features

* add default handler ([c216d8b](https://github.com/kap-sh/zapros/commit/c216d8bc0d2333188b67d3a382a5121cc98b8e03))
* add pyreqwest backend ([0533d82](https://github.com/kap-sh/zapros/commit/0533d82aa085b95c0731cd5822ea222b67d45a53))
* add support for multipart ([459f209](https://github.com/kap-sh/zapros/commit/459f209b1c6d0bdf13e34d8d9b9e730e0af543d7))
