# CHANGELOG



## v8.3.1 (2025-05-18)

### Fix

* fix(es_scan): allow size to be exactly 10000 by changing constraint from lt to le ([`2ad3b5b`](https://github.com/m9810223/esrt/commit/2ad3b5b5ffb2315c56fb80885d4b74383954ee53))

### Unknown

* WIP ([`c387473`](https://github.com/m9810223/esrt/commit/c387473d27e9e6d439ee839431f9b1cd26eefb81))

* WIP ([`1246441`](https://github.com/m9810223/esrt/commit/12464410bd21a003181b5aca49f3ed9d1990bcee))


## v8.3.0 (2025-04-23)

### Feature

* feat: release ([`1e0cf40`](https://github.com/m9810223/esrt/commit/1e0cf40c687f06da2617fac45da27ae267e17f12))


## v8.2.0 (2025-04-21)

### Chore

* chore(release): bump esrt version to 8.2.0

Updated `esrt` version from 8.1.0 to 8.2.0 in `pyproject.toml` and from 8.0.0 to 8.2.0 in `uv.lock` to reflect the latest release version.

No code changes included in this commit — version bump only. ([`b2cf177`](https://github.com/m9810223/esrt/commit/b2cf177652d41185d2ec759bf7b1e717e55572c0))

* chore(cli): replace console.print with console.out for consistency in EsPingCmd

Switched from `console.print` to `console.out` in EsPingCmd for improved consistency in output method, likely to streamline formatting or control over stderr behavior. Also bumped internal package version from 7.0.0 to 8.0.0 in `uv.lock`.

This change assumes `console.out` is a custom abstraction or more appropriate method for CLI output. Ensure it maintains compatibility across usage contexts. ([`ee094fe`](https://github.com/m9810223/esrt/commit/ee094fe513f33a55e12678267e147248df27a924))

### Feature

* feat: release ([`d90fa53`](https://github.com/m9810223/esrt/commit/d90fa53a8bf5ab3149271e2cd5d9ee850eaf5888))

### Unknown

* Merge branch &#39;master&#39; of github.com:m9810223/esrt ([`726a957`](https://github.com/m9810223/esrt/commit/726a95785a9b39f5ee4d10d93b647b2de5392aee))


## v8.1.0 (2025-04-10)

### Feature

* feat: release ([`f17c1b1`](https://github.com/m9810223/esrt/commit/f17c1b151d44ebfb10725dda17ef557b98948b5d))


## v8.0.0 (2025-04-10)

### Breaking

* feat(esrt): switch test input from raw DSL to SQL syntax; improve stdin fallback

- Replace JSON DSL in test-es-sql with SQL queries to match plugin functionality
- Remove `model_validator` from `RequiredInputCmdMixin`, move validation logic to `read_input`
- Add fallback to read from stdin when no input is provided and stdin is not a TTY
- Bump `esrt` version from 6.0.0 to 7.0.0

BREAKING CHANGE: `RequiredInputCmdMixin` no longer raises at validation phase but during execution; CLI behavior may differ for invalid input combinations ([`e645f78`](https://github.com/m9810223/esrt/commit/e645f780c8a9b4ae982bdcf27ce4cfb2391a9212))


## v7.0.0 (2025-04-10)

### Breaking

* feat(esrt): add support for verbose and output options across all ES commands

- Introduced `VerboseCmdMixin` and `OutputCmdMixin` to unify handling of `-v/--verbose` and `-o/--output`
- Applied new mixins to: es_ping, es_request, es_bulk, es_scan, es_search, es_sql
- Refactored and reordered base class composition to ensure consistent CLI behavior
- Added extensive test coverage in `justfile` for new verbose/output/pretty flags
- Improved error messaging for invalid or missing input scenarios
- Renamed `DefaultNoPrettyCmdMixin` → `DefaultNotPrettyCmdMixin` for clarity
- Bumped version from 5.2.0 → 6.0.0 due to breaking interface changes

BREAKING CHANGE: All command mixin compositions have been restructured.
Commands expecting `-v/--verbose` or `-o/--output` now require updated mixin usage. ([`44e2cc0`](https://github.com/m9810223/esrt/commit/44e2cc0bbf9f0408caf04264045720c184346225))


## v6.0.0 (2025-04-03)

### Breaking

* feat: release

BREAKING CHANGE: release ([`d19577b`](https://github.com/m9810223/esrt/commit/d19577b92a02ee3d37e40c48c7861ce73122e4ab))

### Unknown

* Merge branch &#39;master&#39; of github.com:m9810223/esrt ([`18b03fc`](https://github.com/m9810223/esrt/commit/18b03fc07a9d368e25d8484f4806052ba2025857))


## v5.4.0 (2025-04-03)

### Feature

* feat: release

BREAKING CHANGE ([`675958c`](https://github.com/m9810223/esrt/commit/675958c9e831adb2331d82e0c3fd0310baaaeeb9))


## v5.3.0 (2025-04-03)

### Feature

* feat: release ([`52b7784`](https://github.com/m9810223/esrt/commit/52b7784c9e671bfa98bce9f3b260acfa142a72fd))

* feat: release ([`deb7243`](https://github.com/m9810223/esrt/commit/deb7243b8162681d06b7088228aa8b575e104e82))

### Unknown

* Merge branch &#39;master&#39; of github.com:m9810223/esrt ([`d988c5a`](https://github.com/m9810223/esrt/commit/d988c5abfed267d34cadb1eecbcdfeb114c2f0b3))


## v5.2.0 (2025-04-03)

### Feature

* feat: release ([`31df7ed`](https://github.com/m9810223/esrt/commit/31df7eda8b7a5fd0333f6c17358d139200ce339a))

### Unknown

* Merge branch &#39;master&#39; of github.com:m9810223/esrt ([`020b598`](https://github.com/m9810223/esrt/commit/020b59861c47e79d78bb12f7c97206a02baa4799))


## v5.1.0 (2025-04-03)

### Feature

* feat: release ([`b3fb59b`](https://github.com/m9810223/esrt/commit/b3fb59b777493130bf64004418c07caa69428962))


## v5.0.0 (2025-04-01)

### Breaking

* refactor(cmd): unify input mixins and migrate SQL cmd to new structure

- Removed deprecated `_es_sql.py` in favor of `cmd_sql.py` using new mixin pattern
- Renamed and refactored input validation mixins:
  - `JsonInputCmdMixin` ➜ `OptionalInputCmdMixin`
  - `RequiredNdJsonInputCmdMixin` ➜ `RequiredNdInputCmdMixin`
- Introduced `_InputCmdMixin` and `_NdInputCmdMixin` to reduce duplication
- Updated all affected commands (`request`, `scan`, `search`, `bulk`) to use new mixins
- Extended support for `str` input in HTTP body (e.g. for raw text SQL)

BREAKING CHANGE: old `_es_sql.py` script interface is removed; consumers should use the new `sql` subcommand ([`57502e7`](https://github.com/m9810223/esrt/commit/57502e77706e3dd9ccaf5d15bc0b113011ac63cc))

### Unknown

* WIP ([`2142513`](https://github.com/m9810223/esrt/commit/2142513407043e0b4a118f78b7b29e9e90f30387))


## v4.17.0 (2025-03-24)

### Feature

* feat: release ([`ef3beb2`](https://github.com/m9810223/esrt/commit/ef3beb22b3c8a570302d4115fdafa41eca4fa8e9))


## v4.16.0 (2025-03-20)

### Feature

* feat: release ([`dfff47e`](https://github.com/m9810223/esrt/commit/dfff47e3339fe93586aa13c2e0cf42e0175e4f1d))


## v4.15.0 (2025-03-18)

### Feature

* feat: release ([`d3b3c8d`](https://github.com/m9810223/esrt/commit/d3b3c8d2561c829748daa6bc82bcd330f8af4189))

### Unknown

* WIP ([`cd86a32`](https://github.com/m9810223/esrt/commit/cd86a329cefa43a9d298ff3251e723416ce657a1))

* WIP ([`f547ce0`](https://github.com/m9810223/esrt/commit/f547ce0dc079b20196b4af8181eb77c7d0a38c8c))


## v4.14.0 (2025-03-18)

### Feature

* feat: release ([`01bdf5e`](https://github.com/m9810223/esrt/commit/01bdf5edeb93eec387df2fc394ad6fde7f7a14ed))

* feat: release ([`4f0c84b`](https://github.com/m9810223/esrt/commit/4f0c84b0ed061bf6d1200a5fd56623ddb5ec9de5))

### Unknown

* WIP ([`6bd5803`](https://github.com/m9810223/esrt/commit/6bd580359593817622d4a27b3b93686ba38617c3))

* WIP ([`894059d`](https://github.com/m9810223/esrt/commit/894059d4a11cbf0f50aa164c02f017b3c2ec692c))

* WIP ([`5aa5224`](https://github.com/m9810223/esrt/commit/5aa52246140d01feeb7d3f20005a916a1378259f))


## v4.13.0 (2025-03-18)

### Feature

* feat: release ([`c3ab34b`](https://github.com/m9810223/esrt/commit/c3ab34b3f619e0610d07ca83aaff707c19d21c99))

* feat: release ([`11603ce`](https://github.com/m9810223/esrt/commit/11603ce00ef9cb8fd074b0b616a6bc63db6f9fbd))

### Unknown

* WIP ([`b7ac75a`](https://github.com/m9810223/esrt/commit/b7ac75a6b7688d40fc87a7c623b0fb1d5fe2231d))

* WIP ([`2844351`](https://github.com/m9810223/esrt/commit/28443516e493bbe415d3df2dc179282a3be8cbea))

* WIP ([`d647f81`](https://github.com/m9810223/esrt/commit/d647f813ee79340422f67d2a8a9ee57d8d1032fb))

* WIP ([`fb6e9e9`](https://github.com/m9810223/esrt/commit/fb6e9e94ec6b99801e0d27168e6aac3b1bb97cca))

* WIP ([`4331353`](https://github.com/m9810223/esrt/commit/43313533eeb41a3b914a6b3fa63d380c0542fb98))

* WIP ([`f0c0ad1`](https://github.com/m9810223/esrt/commit/f0c0ad1bd8a6f2f4260ffacf7bfbe9318a4457bc))


## v4.12.0 (2025-03-17)

### Feature

* feat: release ([`c1b7e6d`](https://github.com/m9810223/esrt/commit/c1b7e6d21b10466ffc98d88e05fc67d5cedc4511))

### Unknown

* Merge branch &#39;master&#39; of github.com:m9810223/esrt ([`610e344`](https://github.com/m9810223/esrt/commit/610e34467e36f873030e39e31356aeccf4371946))

* WIP ([`36b1d09`](https://github.com/m9810223/esrt/commit/36b1d09c8d6e47e00a1e02b546831945217ced41))


## v4.11.0 (2025-03-17)

### Feature

* feat: release ([`2dc36a3`](https://github.com/m9810223/esrt/commit/2dc36a3e053bcfd4c218654b2d1a0954661f8f29))

### Unknown

* WIP ([`06a382e`](https://github.com/m9810223/esrt/commit/06a382e7398547baa6818f0624c90c83c9999a30))

* Merge branch &#39;master&#39; of github.com:m9810223/esrt ([`5c41b0e`](https://github.com/m9810223/esrt/commit/5c41b0e8720b3a6c45bf795bc58b1b6c74a0ad51))

* WIP ([`ac8ba8d`](https://github.com/m9810223/esrt/commit/ac8ba8d41cd83616b61ea6f1bd589cb946c846d6))


## v4.10.0 (2025-03-17)

### Feature

* feat: release ([`4abc536`](https://github.com/m9810223/esrt/commit/4abc5366524ed90886cc0009460996313c41d7f3))

### Unknown

* WIP ([`fecd5b0`](https://github.com/m9810223/esrt/commit/fecd5b04e41d54560b731a7ad0ab5f95888a0a5c))

* WIP ([`2a919b3`](https://github.com/m9810223/esrt/commit/2a919b3ab5b69b8628cc671d80332ecdc8deb198))


## v4.9.0 (2025-03-17)

### Feature

* feat: release ([`c44c3bb`](https://github.com/m9810223/esrt/commit/c44c3bbf81734a459de8d8483d5716869dab0320))

### Unknown

* WIP ([`ed70de4`](https://github.com/m9810223/esrt/commit/ed70de4d868e11e38293563bfc3a132ce195d725))

* 2025/03/18 06:55:58 ([`3526778`](https://github.com/m9810223/esrt/commit/3526778d1734b5127852d81afb0eabee0c9591cd))


## v4.8.0 (2025-03-17)

### Feature

* feat: release ([`b214383`](https://github.com/m9810223/esrt/commit/b214383d095ba6acffb4ac5c40fe467b4c532a9a))

* feat: release ([`de458fc`](https://github.com/m9810223/esrt/commit/de458fc887128abf15ad7be090b595a0c5c63f47))

* feat: release ([`421d5f7`](https://github.com/m9810223/esrt/commit/421d5f7e554511ecc07ab90e91e70a9f279c96c8))

### Unknown

* WIP ([`0cdbb9c`](https://github.com/m9810223/esrt/commit/0cdbb9c29620d74fec13885d4a9a7d48822a6b88))

* WIP ([`22bd75b`](https://github.com/m9810223/esrt/commit/22bd75b0e2bf042bcb5452f5ba407d293bb33f82))


## v4.7.0 (2025-03-17)

### Feature

* feat: release ([`609e9d2`](https://github.com/m9810223/esrt/commit/609e9d2d7f54d6782f76af5e010b7d629c967689))

### Unknown

* WIP ([`252edec`](https://github.com/m9810223/esrt/commit/252edecb5a3c89e70ad04476559b97355bc9bbd1))


## v4.6.0 (2025-03-17)

### Feature

* feat: release ([`f417bb4`](https://github.com/m9810223/esrt/commit/f417bb4e13e87fd8e1593a4819a7f66fa5ba30c8))

* feat: release ([`96a6b47`](https://github.com/m9810223/esrt/commit/96a6b4777663bf2e309aa6ed7615ec96ee0abc47))


## v4.5.1 (2025-03-16)

### Fix

* fix: release ([`db2e87b`](https://github.com/m9810223/esrt/commit/db2e87bd4dce9565b8b503128c3d6d8b3a612f5a))


## v4.5.0 (2025-03-16)

### Feature

* feat: release ([`d7b5dd2`](https://github.com/m9810223/esrt/commit/d7b5dd2d6bba0f82ec2c00598e67a2c2c4e5ae49))

### Unknown

* WIP ([`1df43b6`](https://github.com/m9810223/esrt/commit/1df43b6edeca5176951475a4b926ffd9d9cb2430))


## v4.4.0 (2025-03-16)

### Feature

* feat: release ([`24bfb4b`](https://github.com/m9810223/esrt/commit/24bfb4b00b70bacf358de6af7ac2475987144a93))

### Unknown

* WIP ([`c74f2ed`](https://github.com/m9810223/esrt/commit/c74f2ed4dd6e29a8e4bfa1888f88e4b36ce46c54))

* WIP ([`f160b5a`](https://github.com/m9810223/esrt/commit/f160b5a7cfc464ff26f3b179bdefd81672c46eaa))


## v4.3.0 (2025-03-16)

### Feature

* feat: release ([`974e80c`](https://github.com/m9810223/esrt/commit/974e80c82c323e583ed43d2a94546165a494ff6e))

### Unknown

* WIP ([`56925e3`](https://github.com/m9810223/esrt/commit/56925e3b248d3cd7cce2664808771e0deabc8b6d))

* WIP ([`3936428`](https://github.com/m9810223/esrt/commit/3936428d8338f4fca7d4e721719a830613f9d38d))

* WIP ([`d79a871`](https://github.com/m9810223/esrt/commit/d79a87147cedac0e7ca5f604ccc507734dac45de))


## v4.2.1 (2025-03-16)

### Fix

* fix: release ([`a89ebb6`](https://github.com/m9810223/esrt/commit/a89ebb61d2d7555d0ea2a3bf1ea1aee06f7bce75))

### Unknown

* WIP ([`525ced9`](https://github.com/m9810223/esrt/commit/525ced97881449b705e9c97f6c3a65c0b44b572d))

* Merge branch &#39;master&#39; of github.com:m9810223/esrt ([`934c3c0`](https://github.com/m9810223/esrt/commit/934c3c0f17535757277d80939a463be779787f9f))

* WIP ([`9df443d`](https://github.com/m9810223/esrt/commit/9df443d0968d5e0e536a8c60151725f420011887))


## v4.2.0 (2025-03-16)

### Feature

* feat: release ([`06719d5`](https://github.com/m9810223/esrt/commit/06719d510994625fcbadb8ae37e3e4fb18a32f3f))

### Unknown

* WIP ([`a62ccb8`](https://github.com/m9810223/esrt/commit/a62ccb84b7aa7071a76d4e41ae6f805f114ca1f0))

* WIP ([`e839869`](https://github.com/m9810223/esrt/commit/e8398696df99bef3bd27c372500cbe59e7915e5e))

* WIP ([`606c4e5`](https://github.com/m9810223/esrt/commit/606c4e5c84ea830eebaab59da91a2ec79d4c0377))

* WIP ([`655449f`](https://github.com/m9810223/esrt/commit/655449f4630dfcb176ae0fe30b4c2ca666804f87))

* WIP ([`2a93058`](https://github.com/m9810223/esrt/commit/2a930584c6d24c1e5a634fa7a6970cb8cac3714f))

* WIP ([`c125ab3`](https://github.com/m9810223/esrt/commit/c125ab3a8b79ff1a66c7c365dd815e3759a16ded))

* WIP ([`e232fd0`](https://github.com/m9810223/esrt/commit/e232fd0ecd7652f06fe7e59d9fe827131e62acd7))

* WIP ([`96b092f`](https://github.com/m9810223/esrt/commit/96b092f86ed6b3b117765bb1ea0950e07cfdda01))

* WIP ([`fae072e`](https://github.com/m9810223/esrt/commit/fae072ee00f3b83be235d04076aaf1e6c0620dd2))


## v4.1.3 (2025-03-16)

### Fix

* fix: release ([`74821ed`](https://github.com/m9810223/esrt/commit/74821ed9bf6eb25cbca6ba14b59b19623e6b21b0))

### Unknown

* Merge branch &#39;master&#39; of github.com:m9810223/esrt ([`6556aad`](https://github.com/m9810223/esrt/commit/6556aad13f4b752ac6818fd9bb93d7915af6ce01))


## v4.1.2 (2025-03-16)

### Fix

* fix: release ([`e35f89c`](https://github.com/m9810223/esrt/commit/e35f89c376b33e87873b4f7afd9ec4f2c0db25bc))


## v4.1.1 (2025-03-16)

### Fix

* fix: release ([`b9b8c05`](https://github.com/m9810223/esrt/commit/b9b8c057d2679bacc7c72a32c4470a93600826d6))

### Unknown

* WIP ([`1a87b39`](https://github.com/m9810223/esrt/commit/1a87b39bc2fa2c9870a8e4a6f29182a369048e37))


## v4.1.0 (2025-03-16)

### Feature

* feat: release ([`946418d`](https://github.com/m9810223/esrt/commit/946418dd5dce8fabbf8d820fbe0a18e2706e338a))


## v4.0.0 (2025-03-16)

### Breaking

* refactor: migrate from PDM to UV and restructure CLI

BREAKING CHANGE:
- Replaced PDM with UV as the package manager (`pdm.lock` removed, `uv.lock` added).
- Changed CLI entry point structure, renaming and reorganizing modules.
- Renamed workflow from `_pdm-publish.yml` to `_pypi-publish.yml` and updated publish steps to use `uv`.
- Updated pre-commit hooks (removed `black`, `pyupgrade`, and `typos`; added `pyproject-fmt`).
- Removed `main.py` as an entry point and adjusted imports accordingly. ([`5c03561`](https://github.com/m9810223/esrt/commit/5c035612b7cc47b1963659416393ebdd355158a9))

### Unknown

* v4 ([`9e35836`](https://github.com/m9810223/esrt/commit/9e3583654ef66ad562277660d97a7d3cd1c186ae))


## v3.3.0 (2024-08-12)

### Feature

* feat: set log level to error ([`eb18aa7`](https://github.com/m9810223/esrt/commit/eb18aa785ade2a3cc0adffa58dc11f3d508b29d1))


## v3.2.0 (2024-08-08)

### Chore

* chore: redirect_stdout ([`8d98a39`](https://github.com/m9810223/esrt/commit/8d98a39c6c02a37692738cd39a40ea2a1df29eba))

* chore: logging color ([`526c545`](https://github.com/m9810223/esrt/commit/526c5456ad796cc751b9b5a81144aa693f433309))

### Feature

* feat: release ([`13b4e3d`](https://github.com/m9810223/esrt/commit/13b4e3d2911c915219f39937b23b08ebc51cb7a3))


## v3.1.0 (2024-08-08)

### Feature

* feat: add logger ([`c3de237`](https://github.com/m9810223/esrt/commit/c3de237ff956f2f79ac54ead8789795314964c49))

### Unknown

* Merge branch &#39;master&#39; of github.com:m9810223/esrt ([`8590009`](https://github.com/m9810223/esrt/commit/85900097273689e59c3147039cd310d435ce8275))


## v3.0.1 (2024-08-08)

### Fix

* fix: Annotated and Optional ([`91c6410`](https://github.com/m9810223/esrt/commit/91c64107b63519ccd61322417810342f3ab3576a))

### Unknown

* Merge branch &#39;master&#39; of github.com:m9810223/esrt ([`b5d3c83`](https://github.com/m9810223/esrt/commit/b5d3c83f8c9b0c91d89b7e92123a6a2844254c34))


## v3.0.0 (2024-08-08)

### Breaking

* feat: refactor

BREAKING CHANGE: refactor ([`6a37f37`](https://github.com/m9810223/esrt/commit/6a37f37eba02ba2b64aeee5447f1b7bcd6b77c35))


## v2.6.2 (2024-08-06)

### Chore

* chore: add main.py ([`5ba9aed`](https://github.com/m9810223/esrt/commit/5ba9aed982b87aefe3cd710a7a4d6fccbfeb9cc1))

### Fix

* fix: type annotation ([`66968e5`](https://github.com/m9810223/esrt/commit/66968e5e313c6b8d5a547cfa13f49381eae30eef))

### Unknown

* fixup! chore: add main.py ([`83bb05b`](https://github.com/m9810223/esrt/commit/83bb05bbe962bcfc419057221236f20058991d5c))


## v2.6.1 (2024-08-06)

### Fix

* fix: cast param `request_timeout` to int ([`ee8d945`](https://github.com/m9810223/esrt/commit/ee8d945aa787b9920e91b87287e04a8b2078058b))


## v2.6.0 (2024-08-06)

### Feature

* feat: refine host ([`09c9909`](https://github.com/m9810223/esrt/commit/09c9909720dd47b1a8804e24b1200adeda13a55d))


## v2.5.0 (2024-08-06)

### Feature

* feat: refine host ([`3080baa`](https://github.com/m9810223/esrt/commit/3080baa035f971c6a8ff9bfb50e4005dd3b040bc))


## v2.4.0 (2024-08-06)

### Feature

* feat: refine host ([`8641785`](https://github.com/m9810223/esrt/commit/8641785d414040ea7345b8575272f7734b130bdf))

* feat: add `certifi` ([`2560d32`](https://github.com/m9810223/esrt/commit/2560d32152747470939ec948f89d4ac70e86e0e0))

### Fix

* fix: remove header value space ([`6b3bd79`](https://github.com/m9810223/esrt/commit/6b3bd79e2ac64602932726fbf04c87743dae810a))

### Unknown

* Merge branch &#39;master&#39; of github.com:m9810223/esrt ([`b83f742`](https://github.com/m9810223/esrt/commit/b83f7426a87ab5dc7e2b526b3661d0ab215ec368))


## v2.3.0 (2024-08-02)

### Feature

* feat: release ([`5611cb6`](https://github.com/m9810223/esrt/commit/5611cb64bb824322e6404ca0d141c1067646ae1c))


## v2.2.0 (2024-07-10)

### Feature

* feat: release ([`f1418f9`](https://github.com/m9810223/esrt/commit/f1418f908300b302b7da20583988a417593087bb))


## v2.1.0 (2024-07-09)

### Feature

* feat: release ([`adee084`](https://github.com/m9810223/esrt/commit/adee084f270bbc4fa7e1380fe533b43c9c30bcdd))


## v2.0.0 (2024-07-09)

### Breaking

* feat: release v2

BREAKING CHANGE: release v2 ([`1df2f9f`](https://github.com/m9810223/esrt/commit/1df2f9fdbbf72c8f17d8fbbeac816e27db62284d))


## v1.35.0 (2024-07-08)

### Feature

* feat: release ([`29f1503`](https://github.com/m9810223/esrt/commit/29f1503529556c40918ae8ef4976313c8a6a57c6))


## v1.34.1 (2024-07-08)

### Fix

* fix: sql ([`67eb589`](https://github.com/m9810223/esrt/commit/67eb58937fbe23eaffb65cf48ee76c7cece96b41))


## v1.34.0 (2024-06-24)

### Feature

* feat: release ([`c91b7b5`](https://github.com/m9810223/esrt/commit/c91b7b5829cc12bfcb74510ffa75836d2da9dae3))


## v1.33.0 (2024-04-12)

### Feature

* feat: release ([`1ee38b3`](https://github.com/m9810223/esrt/commit/1ee38b31cbbb14d418b20a3d2f42ed4a8299ab7e))


## v1.32.0 (2024-04-07)

### Feature

* feat: release ([`9c07c8e`](https://github.com/m9810223/esrt/commit/9c07c8e70bf45990c5847cc23c85e330eaedcbec))

### Unknown

* docs ([`862a180`](https://github.com/m9810223/esrt/commit/862a180f411f5365b0921dd518d28d50e1bc0f62))


## v1.31.0 (2024-04-07)

### Feature

* feat: release ([`3f72863`](https://github.com/m9810223/esrt/commit/3f72863c229c7e107c0d4e35afdd249a13d0416b))


## v1.30.0 (2024-04-07)

### Feature

* feat: release ([`8cbcdbf`](https://github.com/m9810223/esrt/commit/8cbcdbff4e811bf870db65973b83ceefd9e8587d))


## v1.29.0 (2024-04-07)

### Feature

* feat: release ([`e084956`](https://github.com/m9810223/esrt/commit/e084956f046404db6f1beae9a839dbe2f9213e9e))


## v1.28.0 (2024-04-07)

### Feature

* feat: release ([`780a10d`](https://github.com/m9810223/esrt/commit/780a10db3381dd22611e09bb5842b88495596fd6))


## v1.27.0 (2024-04-03)

### Feature

* feat: release ([`bfb243d`](https://github.com/m9810223/esrt/commit/bfb243df98985d260d6b9b116cb0829ef8d5b62d))


## v1.26.0 (2024-04-03)

### Feature

* feat: release ([`8f74890`](https://github.com/m9810223/esrt/commit/8f7489053218a7e211f0399e05548a1ef5ab57cf))


## v1.25.0 (2024-04-03)

### Feature

* feat: release ([`7ac8cb7`](https://github.com/m9810223/esrt/commit/7ac8cb778edc84b4eec24aaf448a5c87f9c7f6c7))

### Unknown

* WIP ([`f239184`](https://github.com/m9810223/esrt/commit/f239184ec584604a8c5bcc89d0b745f47e7b31ee))


## v1.24.0 (2024-04-03)

### Feature

* feat: release ([`b93d614`](https://github.com/m9810223/esrt/commit/b93d6143461d58be78af773422a5a66d1595da6b))


## v1.23.0 (2024-04-03)

### Feature

* feat: release ([`70e7835`](https://github.com/m9810223/esrt/commit/70e78352525cf1ae4f2de54e7b0541b4f6a999a4))


## v1.22.0 (2024-04-01)

### Feature

* feat: envvar `ESRT_TRANSMIT_CHUNK_SIZE` ([`0c0509c`](https://github.com/m9810223/esrt/commit/0c0509cc279097fdd022d88533dee08a4964d1bc))


## v1.21.0 (2024-03-30)

### Feature

* feat: release ([`103e795`](https://github.com/m9810223/esrt/commit/103e7959a7a5729610b8857a5a6d989e333ddff0))


## v1.20.0 (2024-03-30)

### Feature

* feat: release ([`5dce9e5`](https://github.com/m9810223/esrt/commit/5dce9e52b00e557e2f6acf4fe18324ccce4a001d))


## v1.19.0 (2024-03-30)

### Feature

* feat: release ([`95b1d22`](https://github.com/m9810223/esrt/commit/95b1d222f99908555030f00483567f263e57c069))


## v1.18.0 (2024-03-30)

### Feature

* feat: release ([`630ccbc`](https://github.com/m9810223/esrt/commit/630ccbcee4d0c5020066322b2c24933ee49b8fb0))


## v1.17.0 (2024-03-30)

### Feature

* feat: release ([`2a1c1be`](https://github.com/m9810223/esrt/commit/2a1c1be68c25228ac1ccd8b479f4595d6f330693))


## v1.16.0 (2024-03-30)

### Feature

* feat: release ([`ccb72e4`](https://github.com/m9810223/esrt/commit/ccb72e429f2592ade63be1e58961f78d91eb8b92))


## v1.15.0 (2024-03-30)

### Feature

* feat: release ([`286bab3`](https://github.com/m9810223/esrt/commit/286bab376cf1f64e51c3efbaeef5afa7ed955bee))


## v1.14.0 (2024-03-30)

### Feature

* feat: release ([`de0e3f4`](https://github.com/m9810223/esrt/commit/de0e3f4e1f63ddd730c51425c2c2614d63532e11))


## v1.13.0 (2024-03-30)

### Feature

* feat: release ([`9db7756`](https://github.com/m9810223/esrt/commit/9db775649c0097944079c0c9e30aa25dcb07c813))


## v1.12.0 (2024-03-30)

### Feature

* feat: release ([`44b15d0`](https://github.com/m9810223/esrt/commit/44b15d0c3bf668358743b60deda6ea54db118027))


## v1.11.0 (2024-03-30)

### Feature

* feat: release ([`716a5ae`](https://github.com/m9810223/esrt/commit/716a5aeadc418d8875d0d3fa3fec26d0cd7552cb))


## v1.10.0 (2024-03-30)

### Feature

* feat: release ([`624eb48`](https://github.com/m9810223/esrt/commit/624eb487f657490afc46dcbc7d429f2480671fc6))


## v1.9.0 (2024-03-30)

### Feature

* feat: release ([`11b27dc`](https://github.com/m9810223/esrt/commit/11b27dc048beedf05c869e9e2ad901eb95012bdc))


## v1.8.0 (2024-03-28)

### Feature

* feat: release ([`558abc2`](https://github.com/m9810223/esrt/commit/558abc225653662e9f2fa9f447c4c2bb80be87ca))


## v1.7.0 (2024-03-28)

### Feature

* feat: release ([`7fde776`](https://github.com/m9810223/esrt/commit/7fde77619f8d73fc5b1dc87f32134f33cdbe30b9))


## v1.6.0 (2024-03-28)

### Feature

* feat: release ([`f7fd4b5`](https://github.com/m9810223/esrt/commit/f7fd4b5cc398a9d5e6296ae3e5008a822db221d4))


## v1.5.0 (2024-03-28)

### Feature

* feat: release ([`45ff2a6`](https://github.com/m9810223/esrt/commit/45ff2a67d33015ebb94eb5890f8143819e90949d))


## v1.4.0 (2024-03-28)

### Feature

* feat: release ([`b7c473f`](https://github.com/m9810223/esrt/commit/b7c473fb003b31e7e00a85e7bb49ab54fd2c6266))


## v1.3.0 (2024-03-28)

### Feature

* feat: release ([`9311d1e`](https://github.com/m9810223/esrt/commit/9311d1e5ee3ae745dc73ea4938c8fd537fde92b6))


## v1.2.0 (2024-03-28)

### Feature

* feat: release ([`a056b7c`](https://github.com/m9810223/esrt/commit/a056b7c56783db892c3f2447867d05df48ddddc2))


## v1.1.0 (2024-03-27)

### Feature

* feat: release ([`240abda`](https://github.com/m9810223/esrt/commit/240abda8324b75dd997125e1d5d7c57e5bf67148))


## v1.0.0 (2024-03-27)

### Breaking

* feat: release v1

BREAKING CHANGE: release v1 ([`93ee3e4`](https://github.com/m9810223/esrt/commit/93ee3e4c78be8e8e3e1148727e059cdb099d9fbb))


## v0.14.0 (2024-03-27)

### Feature

* feat: release ([`349f168`](https://github.com/m9810223/esrt/commit/349f16833cb26f139d044e7f03908ea3908860b8))


## v0.13.0 (2024-03-27)

### Feature

* feat: release ([`93be503`](https://github.com/m9810223/esrt/commit/93be5032aad95d43f3514f08636852fe319b2504))


## v0.12.0 (2024-03-27)

### Feature

* feat: release ([`c58de91`](https://github.com/m9810223/esrt/commit/c58de917a68249c1c79adf44d5da0f9b4a3de67a))


## v0.11.0 (2024-03-27)

### Feature

* feat: release ([`3446057`](https://github.com/m9810223/esrt/commit/3446057db3d908cdad069a2cbfed30abc457838d))


## v0.10.0 (2024-03-26)

### Feature

* feat: release ([`bfa3232`](https://github.com/m9810223/esrt/commit/bfa3232c471e92821484e033ccd3ec161d09f484))


## v0.9.0 (2024-03-26)

### Feature

* feat: release ([`a9cbd9f`](https://github.com/m9810223/esrt/commit/a9cbd9f45807711461432fea7cd9fac760bd811a))

* feat: release ([`7c33b14`](https://github.com/m9810223/esrt/commit/7c33b14ba7717019523c09db6526901d637127c8))

* feat: release ([`f97a836`](https://github.com/m9810223/esrt/commit/f97a836fc7609456c656ddc1a8c5c6287b814e51))

### Unknown

* Merge branch &#39;master&#39; of github.com:m9810223/esrt ([`72c971b`](https://github.com/m9810223/esrt/commit/72c971b7eda78c1f5faad0393a3177702847eecd))


## v0.8.0 (2024-03-26)

### Feature

* feat: release ([`52e805d`](https://github.com/m9810223/esrt/commit/52e805d1bfaa10eac4a621092af492071bcc2f27))

### Unknown

* Merge branch &#39;master&#39; of github.com:m9810223/esrt ([`3bad3f7`](https://github.com/m9810223/esrt/commit/3bad3f72e8a849737743289ef4c29e357fede1c5))


## v0.7.0 (2024-03-26)

### Feature

* feat: release ([`c640a26`](https://github.com/m9810223/esrt/commit/c640a2609e14b2f8ae7b925f70a31e874e3bcce0))


## v0.6.0 (2024-03-26)

### Feature

* feat: release ([`bbe18c2`](https://github.com/m9810223/esrt/commit/bbe18c25aa78cce2dff2494539099a536045dc19))


## v0.5.0 (2024-03-26)

### Feature

* feat: release ([`a941848`](https://github.com/m9810223/esrt/commit/a941848a026683357b744f0a4fbda6c620c7b48f))

* feat: release ([`5113dfb`](https://github.com/m9810223/esrt/commit/5113dfbd39b13bb3ede6cb5f5135ddd24a10a68e))


## v0.4.0 (2024-03-26)

### Feature

* feat: release ([`48a58e0`](https://github.com/m9810223/esrt/commit/48a58e0cc8804dcbf57f7989758a9b22957ea365))


## v0.3.0 (2024-03-26)

### Feature

* feat: release ([`68c4a41`](https://github.com/m9810223/esrt/commit/68c4a413efe75b042cd2cbb685e6c5f293a535b2))


## v0.2.0 (2024-03-26)

### Feature

* feat: release ([`eafc7b7`](https://github.com/m9810223/esrt/commit/eafc7b7c2caa63762148253968efbfebc412f112))


## v0.1.0 (2024-03-26)

### Feature

* feat: release ([`f08ec85`](https://github.com/m9810223/esrt/commit/f08ec85e4031dc891fcb66d9ebca0eeb00100c99))


## v0.0.0 (2024-03-26)

### Unknown

* wip ([`8ab9377`](https://github.com/m9810223/esrt/commit/8ab9377c368643cf97e500393134a9824764f84e))

* init ([`0b8af51`](https://github.com/m9810223/esrt/commit/0b8af51668548d3609d68e0c47c0afe7ece98b0c))
