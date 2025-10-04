# Changelog

## 2.21.0 (2025-10-03)

Full Changelog: [v2.20.0...v2.21.0](https://github.com/julep-ai/python-sdk/compare/v2.20.0...v2.21.0)

### Features

* **api:** api update ([e685ff8](https://github.com/julep-ai/python-sdk/commit/e685ff8b198b3057f3fd98591d5fd9ea5fb88436))

## 2.20.0 (2025-09-25)

Full Changelog: [v2.19.2...v2.20.0](https://github.com/julep-ai/python-sdk/compare/v2.19.2...v2.20.0)

### Features

* **api:** add auto_run_tools, metadata, and recall_tools to session ([4bcb8b9](https://github.com/julep-ai/python-sdk/commit/4bcb8b983bb90926a8cbd6738ffa494a2f8c27da))
* **api:** api update ([fb19b14](https://github.com/julep-ai/python-sdk/commit/fb19b14fd824747b2d6885e96f0a5a1e2a193f7a))
* **api:** api update ([768c941](https://github.com/julep-ai/python-sdk/commit/768c941e0d29945f08170bf374366c6d0064422b))
* **client:** support file upload requests ([cf64f9c](https://github.com/julep-ai/python-sdk/commit/cf64f9ccf298ec188419faffd68aeed4609c47b9))
* improve future compat with pydantic v3 ([3a1ceb7](https://github.com/julep-ai/python-sdk/commit/3a1ceb7cf1d05be6170fd591c60b3705e099ff50))
* **types:** replace List[str] with SequenceNotStr in params ([85c0d00](https://github.com/julep-ai/python-sdk/commit/85c0d002b08578716f5773be546eb0cea70e6c35))


### Bug Fixes

* avoid newer type syntax ([ab2b07f](https://github.com/julep-ai/python-sdk/commit/ab2b07f9ca94ab97364b3bf9f7bde09d04bfc8ef))
* **compat:** compat with `pydantic&lt;2.8.0` when using additional fields ([754734b](https://github.com/julep-ai/python-sdk/commit/754734b3313e3f9e3daec4b0fdb1885deb2281ab))
* **tests:** update schema types from 'type' to 'string' and 'object' in multiple test files ([f4b6f79](https://github.com/julep-ai/python-sdk/commit/f4b6f79a6f952e19138ad5a88906be65a2cefccb))


### Chores

* do not install brew dependencies in ./scripts/bootstrap by default ([9611b52](https://github.com/julep-ai/python-sdk/commit/9611b520bc8650e254b9989d239a1e30824567bf))
* **internal:** add Sequence related utils ([ae91df8](https://github.com/julep-ai/python-sdk/commit/ae91df87bc3bac07f01ff4835364fc9c6303eb58))
* **internal:** change ci workflow machines ([7d299f1](https://github.com/julep-ai/python-sdk/commit/7d299f17926d0d651234471263d780c8c2dcda9f))
* **internal:** fix ruff target version ([c830640](https://github.com/julep-ai/python-sdk/commit/c8306405a44284f06a7aa58eb1dd3efe2baa1fd6))
* **internal:** move mypy configurations to `pyproject.toml` file ([777fa24](https://github.com/julep-ai/python-sdk/commit/777fa24d36cff98ac152e62f80c64d09e4cd8142))
* **internal:** update comment in script ([1c530b2](https://github.com/julep-ai/python-sdk/commit/1c530b26089dd3d1f6caa64aa9aef3e7901a5ac5))
* **internal:** update pydantic dependency ([c0d79b5](https://github.com/julep-ai/python-sdk/commit/c0d79b5661ab5d651aa09e357e3e9a6aee9d3243))
* **internal:** update pyright exclude list ([ac85eb4](https://github.com/julep-ai/python-sdk/commit/ac85eb4f98440bdcbb70bedfda6f53f30a754912))
* **tests:** simplify `get_platform` test ([d3ce5e9](https://github.com/julep-ai/python-sdk/commit/d3ce5e9a67a7153ae7da76cc3d24ee7a4c54e9f9))
* **types:** change optional parameter type from NotGiven to Omit ([04c2aa0](https://github.com/julep-ai/python-sdk/commit/04c2aa0b230a9c1a7f81e20b3052a79815ee23eb))
* update @stainless-api/prism-cli to v5.15.0 ([e6ad37f](https://github.com/julep-ai/python-sdk/commit/e6ad37f5afb355cfe8056508c1b7628fb111d16b))
* update github action ([6de72a2](https://github.com/julep-ai/python-sdk/commit/6de72a255a7fc4db715044d23af2339146f135e9))

## 2.19.2 (2025-07-25)

Full Changelog: [v2.19.1...v2.19.2](https://github.com/julep-ai/python-sdk/compare/v2.19.1...v2.19.2)

### Bug Fixes

* **parsing:** parse extra field types ([da16c06](https://github.com/julep-ai/python-sdk/commit/da16c062b39ff44bd2613b3a82f7d0ae83d894b9))


### Chores

* **project:** add settings file for vscode ([b205a5a](https://github.com/julep-ai/python-sdk/commit/b205a5ab177bdb328cbe787c6646c6febe84364c))

## 2.19.1 (2025-07-22)

Full Changelog: [v2.19.0...v2.19.1](https://github.com/julep-ai/python-sdk/compare/v2.19.0...v2.19.1)

### Bug Fixes

* **parsing:** ignore empty metadata ([2cb68e9](https://github.com/julep-ai/python-sdk/commit/2cb68e93fad737f7b8b0580daf7ea17d89a45809))


### Chores

* **types:** rebuild Pydantic models after all types are defined ([606b112](https://github.com/julep-ai/python-sdk/commit/606b112bca335f589c094ed6e28123c9c18fe4fd))

## 2.19.0 (2025-07-15)

Full Changelog: [v2.18.0...v2.19.0](https://github.com/julep-ai/python-sdk/compare/v2.18.0...v2.19.0)

### Features

* clean up environment call outs ([aa3d615](https://github.com/julep-ai/python-sdk/commit/aa3d6154cafc047943985abebdf3a91eea141b6a))


### Bug Fixes

* **client:** don't send Content-Type header on GET requests ([9ddb65d](https://github.com/julep-ai/python-sdk/commit/9ddb65d4a70e709487e0647614b32e29bd465efe))

## 2.18.0 (2025-07-11)

Full Changelog: [v2.17.1...v2.18.0](https://github.com/julep-ai/python-sdk/compare/v2.17.1...v2.18.0)

### Features

* **api:** api update ([4f4d574](https://github.com/julep-ai/python-sdk/commit/4f4d5740da2bc1344a597fec84de4261ee7b25ca))


### Chores

* **readme:** fix version rendering on pypi ([5e9d64d](https://github.com/julep-ai/python-sdk/commit/5e9d64d80a56c3f28048c4e4c66de465ffa4ee0f))

## 2.17.1 (2025-07-10)

Full Changelog: [v2.17.0...v2.17.1](https://github.com/julep-ai/python-sdk/compare/v2.17.0...v2.17.1)

### Bug Fixes

* **parsing:** correctly handle nested discriminated unions ([e7c1295](https://github.com/julep-ai/python-sdk/commit/e7c12950c714056a85731981ebccdc1390343751))


### Chores

* **internal:** bump pinned h11 dep ([79b0def](https://github.com/julep-ai/python-sdk/commit/79b0deff7e3520f64f2b935ad1b1dc3786ec9886))
* **internal:** codegen related update ([6d132ba](https://github.com/julep-ai/python-sdk/commit/6d132ba105f0b4cd710f90b8f1ecc0f4767b2e93))
* **package:** mark python 3.13 as supported ([e8af0c1](https://github.com/julep-ai/python-sdk/commit/e8af0c1a096f824209288b85dd2992fe2bd14a68))

## 2.17.0 (2025-07-04)

Full Changelog: [v2.16.0...v2.17.0](https://github.com/julep-ai/python-sdk/compare/v2.16.0...v2.17.0)

### Features

* **api:** api update ([780911b](https://github.com/julep-ai/python-sdk/commit/780911b8a732e231e278c822bccb601f2463b0ff))

## 2.16.0 (2025-07-02)

Full Changelog: [v2.15.2...v2.16.0](https://github.com/julep-ai/python-sdk/compare/v2.15.2...v2.16.0)

### Features

* **api:** api update ([0bfe13d](https://github.com/julep-ai/python-sdk/commit/0bfe13dcc3e35982bc17ae5394813f57a3d03177))


### Chores

* **ci:** change upload type ([3d79847](https://github.com/julep-ai/python-sdk/commit/3d79847232a02c8bff65a20fbad92192d9fa8846))

## 2.15.2 (2025-06-30)

Full Changelog: [v2.15.1...v2.15.2](https://github.com/julep-ai/python-sdk/compare/v2.15.1...v2.15.2)

### Bug Fixes

* **ci:** correct conditional ([1b1778d](https://github.com/julep-ai/python-sdk/commit/1b1778d05ccf133d139e64cbd864e5cb4fcf028b))


### Chores

* **ci:** only run for pushes and fork pull requests ([8283bb5](https://github.com/julep-ai/python-sdk/commit/8283bb5fde69dd47d71799eef8de2dee88f1abbc))

## 2.15.1 (2025-06-27)

Full Changelog: [v2.15.0...v2.15.1](https://github.com/julep-ai/python-sdk/compare/v2.15.0...v2.15.1)

### Bug Fixes

* **ci:** release-doctor — report correct token name ([67188ff](https://github.com/julep-ai/python-sdk/commit/67188ff99a6a0a3cb4003122d89fb510145c97c2))

## 2.15.0 (2025-06-26)

Full Changelog: [v2.14.3...v2.15.0](https://github.com/julep-ai/python-sdk/compare/v2.14.3...v2.15.0)

### Features

* **api:** api update ([1734c15](https://github.com/julep-ai/python-sdk/commit/1734c156b111fd799419a6fda173449a9364150a))

## 2.14.3 (2025-06-25)

Full Changelog: [v2.14.2...v2.14.3](https://github.com/julep-ai/python-sdk/compare/v2.14.2...v2.14.3)

### Chores

* **internal:** codegen related update ([3b6a4b9](https://github.com/julep-ai/python-sdk/commit/3b6a4b9d63ae1b5696eada9197ba24d81e8935cb))

## 2.14.2 (2025-06-24)

Full Changelog: [v2.14.1...v2.14.2](https://github.com/julep-ai/python-sdk/compare/v2.14.1...v2.14.2)

### Chores

* **internal:** version bump ([8a46b62](https://github.com/julep-ai/python-sdk/commit/8a46b62560af371ad941614ffa1d0af2c609fa80))

## 2.14.1 (2025-06-24)

Full Changelog: [v2.14.0...v2.14.1](https://github.com/julep-ai/python-sdk/compare/v2.14.0...v2.14.1)

### Chores

* **tests:** skip some failing tests on the latest python versions ([d65e0ef](https://github.com/julep-ai/python-sdk/commit/d65e0efb5ded3d0df78d577703fe07c38d7afc4c))

## 2.14.0 (2025-06-23)

Full Changelog: [v2.13.0...v2.14.0](https://github.com/julep-ai/python-sdk/compare/v2.13.0...v2.14.0)

### Features

* **api:** api update ([9f2b92b](https://github.com/julep-ai/python-sdk/commit/9f2b92b54f239cd7c7f7ed27ce061dbf407ad6f3))


### Chores

* fix pyproject.toml ([d435d9c](https://github.com/julep-ai/python-sdk/commit/d435d9c11587b779bda5d063e7dd32ba8c3deb16))

## 2.13.0 (2025-06-23)

Full Changelog: [v2.12.0...v2.13.0](https://github.com/julep-ai/python-sdk/compare/v2.12.0...v2.13.0)

### Features

* **api:** api update ([66a9ac1](https://github.com/julep-ai/python-sdk/commit/66a9ac1994e91276dbc15004e6426627b1b151f2))
* **client:** add support for aiohttp ([46d7bd7](https://github.com/julep-ai/python-sdk/commit/46d7bd7e457eda9e0767d4732c0d40743cad444f))

## 2.12.0 (2025-06-19)

Full Changelog: [v2.11.0...v2.12.0](https://github.com/julep-ai/python-sdk/compare/v2.11.0...v2.12.0)

### Features

* **api:** applied suggested fixes ([22a01a8](https://github.com/julep-ai/python-sdk/commit/22a01a88670f94a31072c49ab3407fd221bbe77e))
* **api:** fixes ([3349e34](https://github.com/julep-ai/python-sdk/commit/3349e3472e35258a24b45da9634d53b253d37f59))

## 2.11.0 (2025-06-19)

Full Changelog: [v2.10.0...v2.11.0](https://github.com/julep-ai/python-sdk/compare/v2.10.0...v2.11.0)

### Features

* **client:** add follow_redirects request option ([2ee1435](https://github.com/julep-ai/python-sdk/commit/2ee14355f25b30a4a80931401c48f1c51e3b09a0))


### Bug Fixes

* **client:** correctly parse binary response | stream ([bb822dd](https://github.com/julep-ai/python-sdk/commit/bb822dd04059161a6db37f13712268f4001f6088))
* **tests:** fix: tests which call HTTP endpoints directly with the example parameters ([9f17127](https://github.com/julep-ai/python-sdk/commit/9f17127aaca470f58d7a6f720dc91fa9c4380b41))


### Chores

* **ci:** enable for pull requests ([4461d5e](https://github.com/julep-ai/python-sdk/commit/4461d5edcc8b175c896aad80f427388b452d1859))
* **docs:** remove reference to rye shell ([acbfb68](https://github.com/julep-ai/python-sdk/commit/acbfb68a81a0f1c197b33b4bb7959511545f5176))
* **docs:** remove unnecessary param examples ([66e291e](https://github.com/julep-ai/python-sdk/commit/66e291e0cea554edb5da15a4e105eb46de76d047))
* **internal:** update conftest.py ([1a93922](https://github.com/julep-ai/python-sdk/commit/1a93922b9d71549b44bdc41beb94fa0c12f03f82))
* **readme:** update badges ([afd2518](https://github.com/julep-ai/python-sdk/commit/afd2518be4dc7a881b3502b9c2fcb5ea449136e9))
* **tests:** add tests for httpx client instantiation & proxies ([82132b5](https://github.com/julep-ai/python-sdk/commit/82132b536095da8441b5747431383967c836c044))
* **tests:** run tests in parallel ([131c597](https://github.com/julep-ai/python-sdk/commit/131c59790439ec3bce60e943b8dfa7caf3edc26c))


### Documentation

* **client:** fix httpx.Timeout documentation reference ([0ec016a](https://github.com/julep-ai/python-sdk/commit/0ec016a46a16345bc22e21da216afbefb4898432))

## 2.10.0 (2025-05-30)

Full Changelog: [v2.9.0...v2.10.0](https://github.com/julep-ai/python-sdk/compare/v2.9.0...v2.10.0)

### Features

* **api:** api update ([c425227](https://github.com/julep-ai/python-sdk/commit/c42522777457b78b331e3879779f9204d6272bcb))

## 2.9.0 (2025-05-30)

Full Changelog: [v2.8.0...v2.9.0](https://github.com/julep-ai/python-sdk/compare/v2.8.0...v2.9.0)

### Features

* execution status streaming ([b7d8477](https://github.com/julep-ai/python-sdk/commit/b7d84771a88e915c4b38fedbd994a09b6cf3ec03))


### Bug Fixes

* **api:** update execution status streaming to use correct types and headers ([23c42c5](https://github.com/julep-ai/python-sdk/commit/23c42c5299b33db5555367de6680e1f6482ace25))
* **tests:** assert execution status streaming returns correct type for responses ([803a7eb](https://github.com/julep-ai/python-sdk/commit/803a7eb123e1d0e132860c0dc5fc48ba7f32350c))
* **tests:** correct response.is_closed assertion in TestStatus and TestAsyncStatus ([1c77192](https://github.com/julep-ai/python-sdk/commit/1c771927165c43b146352db20e9ca073f8d70cf9))
* **tests:** enhance type assertion for Stream and AsyncStream in assert_matches_type ([e6336b4](https://github.com/julep-ai/python-sdk/commit/e6336b4130f72605a807d2c50945f3c4762808e2))
* **tests:** lint fix ([be2cb66](https://github.com/julep-ai/python-sdk/commit/be2cb663629e0f4aafcb174e02cde87132a910d8))

## 2.8.0 (2025-05-30)

Full Changelog: [v2.7.0...v2.8.0](https://github.com/julep-ai/python-sdk/compare/v2.7.0...v2.8.0)

### Features

* **api:** manual updates ([025cd74](https://github.com/julep-ai/python-sdk/commit/025cd7426148366347ca971d2922586f32db1163))

## 2.7.0 (2025-05-30)

Full Changelog: [v2.6.0...v2.7.0](https://github.com/julep-ai/python-sdk/compare/v2.6.0...v2.7.0)

### Features

* **api:** api update ([198e606](https://github.com/julep-ai/python-sdk/commit/198e6065c6f92bbd3111f82c396f69a4c61a8f7b))

## 2.6.0 (2025-05-30)

Full Changelog: [v2.5.1...v2.6.0](https://github.com/julep-ai/python-sdk/compare/v2.5.1...v2.6.0)

### Features

* **api:** api update ([7efbf30](https://github.com/julep-ai/python-sdk/commit/7efbf30633fb07e54430681eb538595c1e21fa65))

## 2.5.1 (2025-05-28)

Full Changelog: [v2.5.0...v2.5.1](https://github.com/julep-ai/python-sdk/compare/v2.5.0...v2.5.1)

### Bug Fixes

* **docs/api:** remove references to nonexistent types ([7e678b4](https://github.com/julep-ai/python-sdk/commit/7e678b40ceca3bda2555fbc19b59808a6be8d7bf))

## 2.5.0 (2025-05-26)

Full Changelog: [v2.4.0...v2.5.0](https://github.com/julep-ai/python-sdk/compare/v2.4.0...v2.5.0)

### Features

* **api:** api update ([d2dff79](https://github.com/julep-ai/python-sdk/commit/d2dff790062af4e417969b20e58ced067e67a1d5))

## 2.4.0 (2025-05-26)

Full Changelog: [v2.3.0...v2.4.0](https://github.com/julep-ai/python-sdk/compare/v2.3.0...v2.4.0)

### Features

* **api:** api update ([c2648d4](https://github.com/julep-ai/python-sdk/commit/c2648d460fd72e1cca5c4017ed20aca22827ecaa))

## 2.3.0 (2025-05-24)

Full Changelog: [v2.2.0...v2.3.0](https://github.com/julep-ai/python-sdk/compare/v2.2.0...v2.3.0)

### Features

* **api:** api update ([5de54c9](https://github.com/julep-ai/python-sdk/commit/5de54c9a7c304f0be01711aea4790e0083a8d5c5))

## 2.2.0 (2025-05-24)

Full Changelog: [v2.1.0...v2.2.0](https://github.com/julep-ai/python-sdk/compare/v2.1.0...v2.2.0)

### Features

* **api:** api update ([ff9bca7](https://github.com/julep-ai/python-sdk/commit/ff9bca71b8373ceb0e2d65148edd5076ac0fd7e2))


### Chores

* **docs:** grammar improvements ([dfa258d](https://github.com/julep-ai/python-sdk/commit/dfa258d82cff627ed3054315a0c07875aedc287f))

## 2.1.0 (2025-05-19)

Full Changelog: [v2.0.0...v2.1.0](https://github.com/julep-ai/python-sdk/compare/v2.0.0...v2.1.0)

### Features

* **api:** manual updates ([93a937a](https://github.com/julep-ai/python-sdk/commit/93a937a93571b84649868b24c682bac1d98283f7))

## 2.0.0 (2025-05-16)

Full Changelog: [v1.78.3...v2.0.0](https://github.com/julep-ai/python-sdk/compare/v1.78.3...v2.0.0)

### Features

* **api:** api update ([053aa7e](https://github.com/julep-ai/python-sdk/commit/053aa7ed8c6447bf3e7c41a0fb8d0f537d11c8e1))
* **api:** manual updates ([75655dd](https://github.com/julep-ai/python-sdk/commit/75655dd686306d77228d7293f32c489f11ca2fc7))


### Chores

* **ci:** fix installation instructions ([26c34e0](https://github.com/julep-ai/python-sdk/commit/26c34e0967193c6ee101d7027ffd17b677d5df81))
* **ci:** upload sdks to package manager ([1bcf32d](https://github.com/julep-ai/python-sdk/commit/1bcf32d2ebbdbc85cd733a07760b3e3239e917fd))
* update SDK settings ([f573d02](https://github.com/julep-ai/python-sdk/commit/f573d020c8c057a55e4099e489ff8e0a4117e4d6))

## 1.78.3 (2025-05-10)

Full Changelog: [v1.78.2...v1.78.3](https://github.com/julep-ai/python-sdk/compare/v1.78.2...v1.78.3)

### Bug Fixes

* **package:** support direct resource imports ([0152e0e](https://github.com/julep-ai/python-sdk/commit/0152e0e025fe02f2e0ffdb2e015127c87f53ad29))


### Chores

* broadly detect json family of content-type headers ([e374928](https://github.com/julep-ai/python-sdk/commit/e37492838ff9a9079642c1e97cfe7f35806545db))
* **ci:** only use depot for staging repos ([94a8be8](https://github.com/julep-ai/python-sdk/commit/94a8be8d25b6bc18dce11c11f3538f023f34d7a3))
* **internal:** avoid errors for isinstance checks on proxies ([17bad8a](https://github.com/julep-ai/python-sdk/commit/17bad8a57e3ee8fc380eb17eba80c16353a16cf3))
* **internal:** codegen related update ([2fc5828](https://github.com/julep-ai/python-sdk/commit/2fc58283db4c5000ddf1b322bd74eb772e011e13))
* use lazy imports for resources ([4dd37eb](https://github.com/julep-ai/python-sdk/commit/4dd37eb6026d02e170a4738163a551d9b4e68716))

## 1.78.2 (2025-04-23)

Full Changelog: [v1.78.1...v1.78.2](https://github.com/julep-ai/python-sdk/compare/v1.78.1...v1.78.2)

### Bug Fixes

* **pydantic v1:** more robust ModelField.annotation check ([69040bf](https://github.com/julep-ai/python-sdk/commit/69040bfe38b3409d06e38a44557d04af51c37bd9))


### Chores

* **ci:** add timeout thresholds for CI jobs ([9bcdda4](https://github.com/julep-ai/python-sdk/commit/9bcdda49093f6219a3f65f7e23094a1293db6da1))
* **internal:** fix list file params ([88bbf8b](https://github.com/julep-ai/python-sdk/commit/88bbf8b7fc59e362775a9a068d5fb8109ded9636))
* **internal:** import reformatting ([98e8e43](https://github.com/julep-ai/python-sdk/commit/98e8e433f3ae707a3177aa1c93d7805f91314a8a))
* **internal:** refactor retries to not use recursion ([c495bc8](https://github.com/julep-ai/python-sdk/commit/c495bc89a6d232c4b175ae7cc6f8644fc7f6a086))
* **internal:** update models test ([1a8d8ca](https://github.com/julep-ai/python-sdk/commit/1a8d8ca7259020cc2aacc2e8c74d0586f1aa5294))

## 1.78.1 (2025-04-17)

Full Changelog: [v1.78.0...v1.78.1](https://github.com/julep-ai/python-sdk/compare/v1.78.0...v1.78.1)

### Bug Fixes

* **perf:** optimize some hot paths ([73f14e7](https://github.com/julep-ai/python-sdk/commit/73f14e7264b4fa13de4b0e52fc55e981a4eb7803))
* **perf:** skip traversing types for NotGiven values ([2fcdcd5](https://github.com/julep-ai/python-sdk/commit/2fcdcd53a3a755fc0611b188085f9c252548a0b0))


### Chores

* **client:** minor internal fixes ([84c5466](https://github.com/julep-ai/python-sdk/commit/84c5466b383a130d6588f847487e19bd09736c6b))
* fix typos ([#357](https://github.com/julep-ai/python-sdk/issues/357)) ([5608273](https://github.com/julep-ai/python-sdk/commit/56082733301aab98046eac694d71296e382d0644))
* **internal:** base client updates ([3cd71c5](https://github.com/julep-ai/python-sdk/commit/3cd71c5501c30458ae71d05881aaa67bc69d8432))
* **internal:** bump pyright version ([093bea7](https://github.com/julep-ai/python-sdk/commit/093bea7de0d6663dd351487ee50d53ac17d95f1b))
* **internal:** expand CI branch coverage ([57958c8](https://github.com/julep-ai/python-sdk/commit/57958c83db6953374a965e611da6b68cbc813791))
* **internal:** reduce CI branch coverage ([ab56304](https://github.com/julep-ai/python-sdk/commit/ab563042803abdcc5bd2fe4b7d70df76db156e77))
* **internal:** remove trailing character ([#359](https://github.com/julep-ai/python-sdk/issues/359)) ([20e30a9](https://github.com/julep-ai/python-sdk/commit/20e30a9ea80bf2ff98cb4ee5e9c9fe8f2ae20444))
* **internal:** slight transform perf improvement ([#360](https://github.com/julep-ai/python-sdk/issues/360)) ([40dc868](https://github.com/julep-ai/python-sdk/commit/40dc868256e524f90b7da6f8c69759cd7221d9de))
* **internal:** update pyright settings ([0ecbb7b](https://github.com/julep-ai/python-sdk/commit/0ecbb7b7407f1c87c1b2469e21ab1e52ae213338))

## 1.78.0 (2025-03-20)

Full Changelog: [v1.77.0...v1.78.0](https://github.com/julep-ai/python-sdk/compare/v1.77.0...v1.78.0)

### Features

* **api:** api update ([#353](https://github.com/julep-ai/python-sdk/issues/353)) ([723d15b](https://github.com/julep-ai/python-sdk/commit/723d15bdb92bf00d6417eba04e0714f9643ce9d5))

## 1.77.0 (2025-03-18)

Full Changelog: [v1.76.1...v1.77.0](https://github.com/julep-ai/python-sdk/compare/v1.76.1...v1.77.0)

### Features

* **api:** api update ([#351](https://github.com/julep-ai/python-sdk/issues/351)) ([dd7391b](https://github.com/julep-ai/python-sdk/commit/dd7391bbca5ebb118789b450ff1e8f5f8db68759))


### Bug Fixes

* **ci:** ensure pip is always available ([#348](https://github.com/julep-ai/python-sdk/issues/348)) ([d70c95e](https://github.com/julep-ai/python-sdk/commit/d70c95eb556afad91a7d7b6daa1c6838934f85d6))
* **ci:** remove publishing patch ([#350](https://github.com/julep-ai/python-sdk/issues/350)) ([363ed70](https://github.com/julep-ai/python-sdk/commit/363ed708f34b01b1e7f30ba7a009dbb5d4401e73))

## 1.76.1 (2025-03-15)

Full Changelog: [v1.76.0...v1.76.1](https://github.com/julep-ai/python-sdk/compare/v1.76.0...v1.76.1)

### Bug Fixes

* **types:** handle more discriminated union shapes ([#346](https://github.com/julep-ai/python-sdk/issues/346)) ([1ad81fd](https://github.com/julep-ai/python-sdk/commit/1ad81fd06460654b699ccacfaed2c2e32acca460))


### Chores

* **internal:** bump rye to 0.44.0 ([#344](https://github.com/julep-ai/python-sdk/issues/344)) ([26582f4](https://github.com/julep-ai/python-sdk/commit/26582f451b9978cced4e95ba9521f4fd96df1dd2))

## 1.76.0 (2025-03-14)

Full Changelog: [v1.75.0...v1.76.0](https://github.com/julep-ai/python-sdk/compare/v1.75.0...v1.76.0)

### Features

* **api:** api update ([#342](https://github.com/julep-ai/python-sdk/issues/342)) ([e0de8b5](https://github.com/julep-ai/python-sdk/commit/e0de8b5e92cfb5c555d887c3830f977321e7076b))


### Chores

* **internal:** remove extra empty newlines ([#340](https://github.com/julep-ai/python-sdk/issues/340)) ([a86ee2e](https://github.com/julep-ai/python-sdk/commit/a86ee2ee9c2bd1cecb4d870e42a078d47cf27737))

## 1.75.0 (2025-03-13)

Full Changelog: [v1.74.0...v1.75.0](https://github.com/julep-ai/python-sdk/compare/v1.74.0...v1.75.0)

### Features

* **api:** api update ([#338](https://github.com/julep-ai/python-sdk/issues/338)) ([eab1254](https://github.com/julep-ai/python-sdk/commit/eab1254480c36f2e106af2a0268e8d413a90683b))


### Chores

* **internal:** remove unused http client options forwarding ([#334](https://github.com/julep-ai/python-sdk/issues/334)) ([014b96d](https://github.com/julep-ai/python-sdk/commit/014b96d2a26a113a13c493f72b7062c885f5befa))


### Documentation

* revise readme docs about nested params ([#336](https://github.com/julep-ai/python-sdk/issues/336)) ([6ba13aa](https://github.com/julep-ai/python-sdk/commit/6ba13aac39a59f309b2b29cb9e59841e785e74dc))

## 1.74.0 (2025-03-04)

Full Changelog: [v1.73.0...v1.74.0](https://github.com/julep-ai/python-sdk/compare/v1.73.0...v1.74.0)

### Features

* **api:** api update ([#331](https://github.com/julep-ai/python-sdk/issues/331)) ([bb35c4b](https://github.com/julep-ai/python-sdk/commit/bb35c4b6ae6ddba3970da48619c7d938d5b16174))

## 1.73.0 (2025-03-01)

Full Changelog: [v1.72.0...v1.73.0](https://github.com/julep-ai/python-sdk/compare/v1.72.0...v1.73.0)

### Features

* **api:** manual updates ([#328](https://github.com/julep-ai/python-sdk/issues/328)) ([b52cba0](https://github.com/julep-ai/python-sdk/commit/b52cba007de86b8a87f9791659dbb0aa8e81a233))

## 1.72.0 (2025-03-01)

Full Changelog: [v1.71.0...v1.72.0](https://github.com/julep-ai/python-sdk/compare/v1.71.0...v1.72.0)

### Features

* **api:** api update ([#325](https://github.com/julep-ai/python-sdk/issues/325)) ([e6ad6e2](https://github.com/julep-ai/python-sdk/commit/e6ad6e26d1b67c9528cfc14799196c31ece3da30))

## 1.71.0 (2025-02-28)

Full Changelog: [v1.70.0...v1.71.0](https://github.com/julep-ai/python-sdk/compare/v1.70.0...v1.71.0)

### Features

* **api:** api update ([#323](https://github.com/julep-ai/python-sdk/issues/323)) ([58266d0](https://github.com/julep-ai/python-sdk/commit/58266d0ef5151adbb4f5b00b5da58053b9e404a1))


### Chores

* **docs:** update client docstring ([#321](https://github.com/julep-ai/python-sdk/issues/321)) ([e64cb63](https://github.com/julep-ai/python-sdk/commit/e64cb63fdd6c2df725ac71eb89fcd025652ddaca))


### Documentation

* update URLs from stainlessapi.com to stainless.com ([#320](https://github.com/julep-ai/python-sdk/issues/320)) ([fc1f8bc](https://github.com/julep-ai/python-sdk/commit/fc1f8bca544087862bace8cd45ce3dd47acfa21c))

## 1.70.0 (2025-02-27)

Full Changelog: [v1.69.0...v1.70.0](https://github.com/julep-ai/python-sdk/compare/v1.69.0...v1.70.0)

### Features

* **api:** api update ([#317](https://github.com/julep-ai/python-sdk/issues/317)) ([94b0fed](https://github.com/julep-ai/python-sdk/commit/94b0fed6749a73da3a83e62c63ccde335bc55168))

## 1.69.0 (2025-02-27)

Full Changelog: [v1.68.0...v1.69.0](https://github.com/julep-ai/python-sdk/compare/v1.68.0...v1.69.0)

### Features

* **api:** api update ([#314](https://github.com/julep-ai/python-sdk/issues/314)) ([773fc8d](https://github.com/julep-ai/python-sdk/commit/773fc8d8197e322104a6afcf976f0d668ce30621))

## 1.68.0 (2025-02-26)

Full Changelog: [v1.67.0...v1.68.0](https://github.com/julep-ai/python-sdk/compare/v1.67.0...v1.68.0)

### Features

* **api:** api update ([#312](https://github.com/julep-ai/python-sdk/issues/312)) ([b9c6dc9](https://github.com/julep-ai/python-sdk/commit/b9c6dc957423cd040f45ee353b7f7401d9a2b58f))


### Chores

* **internal:** properly set __pydantic_private__ ([#310](https://github.com/julep-ai/python-sdk/issues/310)) ([794fa72](https://github.com/julep-ai/python-sdk/commit/794fa72485e0662ff6681f96e41cc6bf1fdba733))

## 1.67.0 (2025-02-25)

Full Changelog: [v1.66.0...v1.67.0](https://github.com/julep-ai/python-sdk/compare/v1.66.0...v1.67.0)

### Features

* **api:** api update ([#306](https://github.com/julep-ai/python-sdk/issues/306)) ([686e99e](https://github.com/julep-ai/python-sdk/commit/686e99eb76a7e0ac96b44e2c25f2c9719e27d858))
* **api:** api update ([#307](https://github.com/julep-ai/python-sdk/issues/307)) ([46d4ea9](https://github.com/julep-ai/python-sdk/commit/46d4ea965381e079e67799d932b52391378361bc))

## 1.66.0 (2025-02-24)

Full Changelog: [v1.65.0...v1.66.0](https://github.com/julep-ai/python-sdk/compare/v1.65.0...v1.66.0)

### Features

* **api:** api update ([#303](https://github.com/julep-ai/python-sdk/issues/303)) ([07abd73](https://github.com/julep-ai/python-sdk/commit/07abd733ac71fa9850511069338ce4ba4cc1b62b))

## 1.65.0 (2025-02-24)

Full Changelog: [v1.64.0...v1.65.0](https://github.com/julep-ai/python-sdk/compare/v1.64.0...v1.65.0)

### Features

* **api:** api update ([#301](https://github.com/julep-ai/python-sdk/issues/301)) ([d9be600](https://github.com/julep-ai/python-sdk/commit/d9be6006a9740aef6e7f62f3ec8a6239ce496cb8))


### Chores

* **internal:** fix devcontainers setup ([#299](https://github.com/julep-ai/python-sdk/issues/299)) ([82ba8f7](https://github.com/julep-ai/python-sdk/commit/82ba8f75000b03608bef78d87bad71cc5291412e))

## 1.64.0 (2025-02-21)

Full Changelog: [v1.63.0...v1.64.0](https://github.com/julep-ai/python-sdk/compare/v1.63.0...v1.64.0)

### Features

* **client:** allow passing `NotGiven` for body ([#296](https://github.com/julep-ai/python-sdk/issues/296)) ([8dae935](https://github.com/julep-ai/python-sdk/commit/8dae93507a5a0865d9b729bd7b0df574a2b59641))


### Bug Fixes

* **client:** mark some request bodies as optional ([8dae935](https://github.com/julep-ai/python-sdk/commit/8dae93507a5a0865d9b729bd7b0df574a2b59641))

## 1.63.0 (2025-02-18)

Full Changelog: [v1.62.0...v1.63.0](https://github.com/julep-ai/python-sdk/compare/v1.62.0...v1.63.0)

### Features

* **api:** api update ([#293](https://github.com/julep-ai/python-sdk/issues/293)) ([dd5ceec](https://github.com/julep-ai/python-sdk/commit/dd5ceec8214f6884226250ae910d79e1b06f81df))

## 1.62.0 (2025-02-17)

Full Changelog: [v1.61.0...v1.62.0](https://github.com/julep-ai/python-sdk/compare/v1.61.0...v1.62.0)

### Features

* **api:** api update ([#291](https://github.com/julep-ai/python-sdk/issues/291)) ([ae28070](https://github.com/julep-ai/python-sdk/commit/ae28070b3a67cdfa7f554e3452e51e6471d1c22d))


### Bug Fixes

* asyncify on non-asyncio runtimes ([#290](https://github.com/julep-ai/python-sdk/issues/290)) ([30812e2](https://github.com/julep-ai/python-sdk/commit/30812e2a95ba501c4ee0b4d15ca5b403036cfede))


### Chores

* **internal:** update client tests ([#288](https://github.com/julep-ai/python-sdk/issues/288)) ([5732cf0](https://github.com/julep-ai/python-sdk/commit/5732cf04568a0fa2bc2fea1f15659790e9154b55))

## 1.61.0 (2025-02-08)

Full Changelog: [v1.60.0...v1.61.0](https://github.com/julep-ai/python-sdk/compare/v1.60.0...v1.61.0)

### Features

* feat: Add cli as optional dependency ([96f75ea](https://github.com/julep-ai/python-sdk/commit/96f75ea71da55e26e747ea828a440a63a7be0d53))

## 1.60.0 (2025-02-08)

Full Changelog: [v1.59.0...v1.60.0](https://github.com/julep-ai/python-sdk/compare/v1.59.0...v1.60.0)

### Features

* **api:** api update ([#280](https://github.com/julep-ai/python-sdk/issues/280)) ([0061af7](https://github.com/julep-ai/python-sdk/commit/0061af77f2412399d1f6068f075d621001a8f9b2))
* **client:** send `X-Stainless-Read-Timeout` header ([#281](https://github.com/julep-ai/python-sdk/issues/281)) ([78f5704](https://github.com/julep-ai/python-sdk/commit/78f5704d062edf91ee572181b64b437ac4188959))


### Chores

* **internal:** bummp ruff dependency ([#278](https://github.com/julep-ai/python-sdk/issues/278)) ([18ef865](https://github.com/julep-ai/python-sdk/commit/18ef86563c00ab2fdb13cd1d7aad4e3b01281a22))
* **internal:** fix type traversing dictionary params ([#282](https://github.com/julep-ai/python-sdk/issues/282)) ([04ee337](https://github.com/julep-ai/python-sdk/commit/04ee3371be2ec4a71cb3fc87fe2ec73081819137))
* **internal:** minor type handling changes ([#283](https://github.com/julep-ai/python-sdk/issues/283)) ([c60e889](https://github.com/julep-ai/python-sdk/commit/c60e889e1e1a478fae1328e230911d02c4013505))

## 1.59.0 (2025-02-04)

Full Changelog: [v1.58.0...v1.59.0](https://github.com/julep-ai/python-sdk/compare/v1.58.0...v1.59.0)

### Features

* **api:** api update ([#274](https://github.com/julep-ai/python-sdk/issues/274)) ([3a151a2](https://github.com/julep-ai/python-sdk/commit/3a151a2f6f8d0f9b025d602e5d9edee2827e6cdd))


### Chores

* **internal:** change default timeout to an int ([#276](https://github.com/julep-ai/python-sdk/issues/276)) ([570ef97](https://github.com/julep-ai/python-sdk/commit/570ef975c241178691ecdf77d5d90f8871f28cf4))

## 1.58.0 (2025-01-28)

Full Changelog: [v1.57.0...v1.58.0](https://github.com/julep-ai/python-sdk/compare/v1.57.0...v1.58.0)

### Features

* **api:** api update ([#272](https://github.com/julep-ai/python-sdk/issues/272)) ([c70f814](https://github.com/julep-ai/python-sdk/commit/c70f81462190c5698010bec3e7d19c0afa5e3002))


### Chores

* **internal:** codegen related update ([#270](https://github.com/julep-ai/python-sdk/issues/270)) ([6729d49](https://github.com/julep-ai/python-sdk/commit/6729d49bf43eb301971bfeb9d0ecddc218d21c2c))

## 1.57.0 (2025-01-27)

Full Changelog: [v1.56.0...v1.57.0](https://github.com/julep-ai/python-sdk/compare/v1.56.0...v1.57.0)

### Features

* **api:** api update ([#267](https://github.com/julep-ai/python-sdk/issues/267)) ([252b09a](https://github.com/julep-ai/python-sdk/commit/252b09aa70f87df910a16883ee872e59d386ff0a))

## 1.56.0 (2025-01-22)

Full Changelog: [v1.55.1...v1.56.0](https://github.com/julep-ai/python-sdk/compare/v1.55.1...v1.56.0)

### Features

* **api:** api update ([#265](https://github.com/julep-ai/python-sdk/issues/265)) ([038234c](https://github.com/julep-ai/python-sdk/commit/038234c1f2c6a71546e6f786fce8cc6ee9c024c8))


### Chores

* **internal:** codegen related update ([#263](https://github.com/julep-ai/python-sdk/issues/263)) ([84b9918](https://github.com/julep-ai/python-sdk/commit/84b99188d6d81a360b4c51626da1c99b7795c3f9))

## 1.55.1 (2025-01-21)

Full Changelog: [v1.55.0...v1.55.1](https://github.com/julep-ai/python-sdk/compare/v1.55.0...v1.55.1)

### Bug Fixes

* **tests:** make test_get_platform less flaky ([#260](https://github.com/julep-ai/python-sdk/issues/260)) ([1ae47e0](https://github.com/julep-ai/python-sdk/commit/1ae47e01d6353582097f8c2635cd0492b4ad72e7))


### Chores

* **internal:** codegen related update ([#256](https://github.com/julep-ai/python-sdk/issues/256)) ([af7f193](https://github.com/julep-ai/python-sdk/commit/af7f193c4c129f1df40f09136d94e724513de26f))
* **internal:** codegen related update ([#258](https://github.com/julep-ai/python-sdk/issues/258)) ([f705d27](https://github.com/julep-ai/python-sdk/commit/f705d275e5e829ae47d37723067458337a07452d))


### Documentation

* **raw responses:** fix duplicate `the` ([#259](https://github.com/julep-ai/python-sdk/issues/259)) ([06a6a4b](https://github.com/julep-ai/python-sdk/commit/06a6a4beff581a7e501bb3f812dfdd852dc0f977))

## 1.55.0 (2025-01-16)

Full Changelog: [v1.54.0...v1.55.0](https://github.com/julep-ai/python-sdk/compare/v1.54.0...v1.55.0)

### Features

* **api:** api update ([#253](https://github.com/julep-ai/python-sdk/issues/253)) ([9bf4d32](https://github.com/julep-ai/python-sdk/commit/9bf4d32e530bd83edb1d30cce7d224c98c7e974a))

## 1.54.0 (2025-01-16)

Full Changelog: [v1.53.0...v1.54.0](https://github.com/julep-ai/python-sdk/compare/v1.53.0...v1.54.0)

### Features

* **api:** api update ([#249](https://github.com/julep-ai/python-sdk/issues/249)) ([467b9e8](https://github.com/julep-ai/python-sdk/commit/467b9e803f4b5e2f5377ae84c73b14c607a8f969))
* **api:** api update ([#250](https://github.com/julep-ai/python-sdk/issues/250)) ([8b27a43](https://github.com/julep-ai/python-sdk/commit/8b27a4366a2ac9562ed7357ccd753a9f33d1f7a3))
* **api:** Switch default environment to production ([#247](https://github.com/julep-ai/python-sdk/issues/247)) ([d81da34](https://github.com/julep-ai/python-sdk/commit/d81da34aea281c01fd0e933f17d01c2c01e53a42))
* **api:** Switch default environment to production ([#251](https://github.com/julep-ai/python-sdk/issues/251)) ([a058b47](https://github.com/julep-ai/python-sdk/commit/a058b471ef493da954ec4de960dc625bbeb0f71e))

## 1.53.0 (2025-01-14)

Full Changelog: [v1.52.0...v1.53.0](https://github.com/julep-ai/python-sdk/compare/v1.52.0...v1.53.0)

### Features

* **api:** put/patch methods swap ([#244](https://github.com/julep-ai/python-sdk/issues/244)) ([0455920](https://github.com/julep-ai/python-sdk/commit/0455920f814ab7457a065596b944110ee091cee8))

## 1.52.0 (2025-01-13)

Full Changelog: [v1.51.0...v1.52.0](https://github.com/julep-ai/python-sdk/compare/v1.51.0...v1.52.0)

### Features

* **api:** api update ([#241](https://github.com/julep-ai/python-sdk/issues/241)) ([8483cfc](https://github.com/julep-ai/python-sdk/commit/8483cfcd725c22695bd9327c4b95c13582507ccd))

## 1.51.0 (2025-01-13)

Full Changelog: [v1.50.0...v1.51.0](https://github.com/julep-ai/python-sdk/compare/v1.50.0...v1.51.0)

### Features

* **api:** api update ([#238](https://github.com/julep-ai/python-sdk/issues/238)) ([9bd606c](https://github.com/julep-ai/python-sdk/commit/9bd606c48996b39fd49f1679bbec76777de985bc))

## 1.50.0 (2025-01-11)

Full Changelog: [v1.49.0...v1.50.0](https://github.com/julep-ai/python-sdk/compare/v1.49.0...v1.50.0)

### Features

* **api:** api update ([#235](https://github.com/julep-ai/python-sdk/issues/235)) ([d108e64](https://github.com/julep-ai/python-sdk/commit/d108e647a1d4ac6007d312969c2fbe7208087819))

## 1.49.0 (2025-01-10)

Full Changelog: [v1.48.1...v1.49.0](https://github.com/julep-ai/python-sdk/compare/v1.48.1...v1.49.0)

### Features

* **api:** api update ([#233](https://github.com/julep-ai/python-sdk/issues/233)) ([cb53a63](https://github.com/julep-ai/python-sdk/commit/cb53a634c37bbdca494b4d2fe61375199a6535ae))


### Chores

* **internal:** codegen related update ([#232](https://github.com/julep-ai/python-sdk/issues/232)) ([e98f272](https://github.com/julep-ai/python-sdk/commit/e98f272ef2be9e0dae8d1b14806f3c2af25a8988))


### Documentation

* fix typos ([#230](https://github.com/julep-ai/python-sdk/issues/230)) ([4befc05](https://github.com/julep-ai/python-sdk/commit/4befc050986f7d00c77a74e2efb25cbd0837a924))

## 1.48.1 (2025-01-08)

Full Changelog: [v1.48.0...v1.48.1](https://github.com/julep-ai/python-sdk/compare/v1.48.0...v1.48.1)

### Bug Fixes

* **client:** only call .close() when needed ([#228](https://github.com/julep-ai/python-sdk/issues/228)) ([520a500](https://github.com/julep-ai/python-sdk/commit/520a500e23414b91dba825175418101c517206ec))


### Chores

* add missing isclass check ([#225](https://github.com/julep-ai/python-sdk/issues/225)) ([ca9c559](https://github.com/julep-ai/python-sdk/commit/ca9c559a1b0818a87dd20dee2e3d1575a302535a))
* **client:** simplify `Optional[object]` to just `object` ([#223](https://github.com/julep-ai/python-sdk/issues/223)) ([432e8a2](https://github.com/julep-ai/python-sdk/commit/432e8a2d35179669a693793b487b8d4a05ff2296))
* **internal:** bump httpx dependency ([#226](https://github.com/julep-ai/python-sdk/issues/226)) ([76d94df](https://github.com/julep-ai/python-sdk/commit/76d94dfb60d4b79bc62af019f25d39b6e4293748))
* **internal:** update examples ([#227](https://github.com/julep-ai/python-sdk/issues/227)) ([ac2fa0c](https://github.com/julep-ai/python-sdk/commit/ac2fa0cb21ca92c1f8af700a35e8b4b91f430d4e))

## 1.48.0 (2025-01-05)

Full Changelog: [v1.47.0...v1.48.0](https://github.com/julep-ai/python-sdk/compare/v1.47.0...v1.48.0)

### Features

* **api:** api update ([#220](https://github.com/julep-ai/python-sdk/issues/220)) ([9aaf47d](https://github.com/julep-ai/python-sdk/commit/9aaf47d54b9d8eb672c75661b998ccd294954568))

## 1.47.0 (2025-01-05)

Full Changelog: [v1.46.3...v1.47.0](https://github.com/julep-ai/python-sdk/compare/v1.46.3...v1.47.0)

### Features

* **api:** api update ([#217](https://github.com/julep-ai/python-sdk/issues/217)) ([e533ded](https://github.com/julep-ai/python-sdk/commit/e533dedbc1a7e1639c22fa165caec5f6364100b1))

## 1.46.3 (2025-01-02)

Full Changelog: [v1.46.2...v1.46.3](https://github.com/julep-ai/python-sdk/compare/v1.46.2...v1.46.3)

### Chores

* **internal:** codegen related update ([#214](https://github.com/julep-ai/python-sdk/issues/214)) ([6bf9867](https://github.com/julep-ai/python-sdk/commit/6bf98679506bf2750fc1cb20f5a74848bd92dd1b))

## 1.46.2 (2024-12-19)

Full Changelog: [v1.46.1...v1.46.2](https://github.com/julep-ai/python-sdk/compare/v1.46.1...v1.46.2)

### Chores

* **internal:** codegen related update ([#204](https://github.com/julep-ai/python-sdk/issues/204)) ([bcf74cc](https://github.com/julep-ai/python-sdk/commit/bcf74ccacb6bbc55eee0a134a51c9c45814c938e))
* **internal:** codegen related update ([#206](https://github.com/julep-ai/python-sdk/issues/206)) ([330b37a](https://github.com/julep-ai/python-sdk/commit/330b37a15d633e1b8116c52e36db8d2a652e836d))
* **internal:** codegen related update ([#207](https://github.com/julep-ai/python-sdk/issues/207)) ([9f14f2e](https://github.com/julep-ai/python-sdk/commit/9f14f2e5d5be874cb2c428d4ed7d772afc0a51c8))
* **internal:** codegen related update ([#208](https://github.com/julep-ai/python-sdk/issues/208)) ([a4efd84](https://github.com/julep-ai/python-sdk/commit/a4efd8460884d375eb1f457e12479eeb30d5a626))
* **internal:** codegen related update ([#209](https://github.com/julep-ai/python-sdk/issues/209)) ([a5d3c7e](https://github.com/julep-ai/python-sdk/commit/a5d3c7e250b805512f5074f13d5d290eceadd776))
* **internal:** codegen related update ([#210](https://github.com/julep-ai/python-sdk/issues/210)) ([095d0ae](https://github.com/julep-ai/python-sdk/commit/095d0ae75417640ea103887725b547509fa676ab))
* **internal:** codegen related update ([#211](https://github.com/julep-ai/python-sdk/issues/211)) ([3322047](https://github.com/julep-ai/python-sdk/commit/3322047a5c02c23824a3969173fef776db2ee165))
* **internal:** codegen related update ([#212](https://github.com/julep-ai/python-sdk/issues/212)) ([0e07c5b](https://github.com/julep-ai/python-sdk/commit/0e07c5b6a47eccafc530f2daff691b9fe4827013))

## 1.46.1 (2024-12-13)

Full Changelog: [v1.46.0...v1.46.1](https://github.com/julep-ai/python-sdk/compare/v1.46.0...v1.46.1)

### Chores

* **internal:** add support for TypeAliasType ([#202](https://github.com/julep-ai/python-sdk/issues/202)) ([25acb40](https://github.com/julep-ai/python-sdk/commit/25acb40c091ce67316828d2eeb65992335d5bae8))
* **internal:** bump pyright ([#200](https://github.com/julep-ai/python-sdk/issues/200)) ([e62893a](https://github.com/julep-ai/python-sdk/commit/e62893add4117e2efba9cc63fdc206c53fe662e0))

## 1.46.0 (2024-12-13)

Full Changelog: [v1.45.0...v1.46.0](https://github.com/julep-ai/python-sdk/compare/v1.45.0...v1.46.0)

### Features

* **api:** api update ([#198](https://github.com/julep-ai/python-sdk/issues/198)) ([4af80f9](https://github.com/julep-ai/python-sdk/commit/4af80f914d427a302514e7829ab77c8cc36290a8))


### Chores

* **internal:** bump pydantic dependency ([#195](https://github.com/julep-ai/python-sdk/issues/195)) ([72c124c](https://github.com/julep-ai/python-sdk/commit/72c124c256bb9e3fa25381e2b132c2e3b0b5cc6e))


### Documentation

* **readme:** fix http client proxies example ([#197](https://github.com/julep-ai/python-sdk/issues/197)) ([5b788c0](https://github.com/julep-ai/python-sdk/commit/5b788c05da8ae426c18c0925c4c8a65928da5706))

## 1.45.0 (2024-12-07)

Full Changelog: [v1.44.1...v1.45.0](https://github.com/julep-ai/python-sdk/compare/v1.44.1...v1.45.0)

### Features

* **api:** api update ([#192](https://github.com/julep-ai/python-sdk/issues/192)) ([459d332](https://github.com/julep-ai/python-sdk/commit/459d332faee2829eccc3ed52445ad90eaadbe22c))

## 1.44.1 (2024-12-06)

Full Changelog: [v1.44.0...v1.44.1](https://github.com/julep-ai/python-sdk/compare/v1.44.0...v1.44.1)

### Chores

* **internal:** bump pyright ([#187](https://github.com/julep-ai/python-sdk/issues/187)) ([b6b1cba](https://github.com/julep-ai/python-sdk/commit/b6b1cba69fb4e4f5d07744e19da56e66608517ab))
* make the `Omit` type public ([#189](https://github.com/julep-ai/python-sdk/issues/189)) ([e3c45ce](https://github.com/julep-ai/python-sdk/commit/e3c45cea55ef4cb90f53bee603efc171566f69bf))

## 1.44.0 (2024-12-03)

Full Changelog: [v1.43.1...v1.44.0](https://github.com/julep-ai/python-sdk/compare/v1.43.1...v1.44.0)

### Features

* **api:** api update ([#184](https://github.com/julep-ai/python-sdk/issues/184)) ([21b0d04](https://github.com/julep-ai/python-sdk/commit/21b0d04a2c763710bb55e367ad62b05e0de2b47e))

## 1.43.1 (2024-11-28)

Full Changelog: [v1.43.0...v1.43.1](https://github.com/julep-ai/python-sdk/compare/v1.43.0...v1.43.1)

### Bug Fixes

* **client:** compat with new httpx 0.28.0 release ([#182](https://github.com/julep-ai/python-sdk/issues/182)) ([d585c22](https://github.com/julep-ai/python-sdk/commit/d585c2290a69f6816455869b45edfa1a8094460b))


### Chores

* **internal:** exclude mypy from running on tests ([#180](https://github.com/julep-ai/python-sdk/issues/180)) ([187d984](https://github.com/julep-ai/python-sdk/commit/187d984f3b356c399f51fb08c73a402869744582))

## 1.43.0 (2024-11-27)

Full Changelog: [v1.42.1...v1.43.0](https://github.com/julep-ai/python-sdk/compare/v1.42.1...v1.43.0)

### Features

* fix: Fix extra keyword args ([c2ac39d](https://github.com/julep-ai/python-sdk/commit/c2ac39d74a5116b3014e2830bda3711d155aab64))

## 1.42.1 (2024-11-26)

Full Changelog: [v1.42.0...v1.42.1](https://github.com/julep-ai/python-sdk/compare/v1.42.0...v1.42.1)

### Chores

* **internal:** codegen related update ([#175](https://github.com/julep-ai/python-sdk/issues/175)) ([d058571](https://github.com/julep-ai/python-sdk/commit/d058571beb49ea1ea9101ea5b6622fa2b6ea679c))
* **internal:** fix compat model_dump method when warnings are passed ([#171](https://github.com/julep-ai/python-sdk/issues/171)) ([45fdda6](https://github.com/julep-ai/python-sdk/commit/45fdda6fdca71cbaefc86332dcc73e1a2a173f1a))


### Documentation

* add info log level to readme ([#173](https://github.com/julep-ai/python-sdk/issues/173)) ([7eb93ee](https://github.com/julep-ai/python-sdk/commit/7eb93eefb33c11f8186962cf20fc2caec3de49d6))

## 1.42.0 (2024-11-22)

Full Changelog: [v1.41.0...v1.42.0](https://github.com/julep-ai/python-sdk/compare/v1.41.0...v1.42.0)

### Features

* **api:** add files endpoints ([#168](https://github.com/julep-ai/python-sdk/issues/168)) ([83b7828](https://github.com/julep-ai/python-sdk/commit/83b78286db151fa439b377261a30ae77331c3ff6))

## 1.41.0 (2024-11-20)

Full Changelog: [v1.40.0...v1.41.0](https://github.com/julep-ai/python-sdk/compare/v1.40.0...v1.41.0)

### Features

* **api:** api update ([#166](https://github.com/julep-ai/python-sdk/issues/166)) ([041b30a](https://github.com/julep-ai/python-sdk/commit/041b30a4a5fa5ff86e873b46c8ba0b76b4a6fb9a))


### Chores

* rebuild project due to codegen change ([#163](https://github.com/julep-ai/python-sdk/issues/163)) ([e7d75c5](https://github.com/julep-ai/python-sdk/commit/e7d75c5d4b2cabbe64d8f58b9bd6e3f7b6193af7))
* rebuild project due to codegen change ([#165](https://github.com/julep-ai/python-sdk/issues/165)) ([b99f7bb](https://github.com/julep-ai/python-sdk/commit/b99f7bba13ee64150db4e396882d22ede28429cd))

## 1.40.0 (2024-11-16)

Full Changelog: [v1.39.0...v1.40.0](https://github.com/julep-ai/python-sdk/compare/v1.39.0...v1.40.0)

### Features

* **api:** increase retries ([#160](https://github.com/julep-ai/python-sdk/issues/160)) ([6ab6ffc](https://github.com/julep-ai/python-sdk/commit/6ab6ffc36e1af790c32db5276b6ac0f5bccd7759))

## 1.39.0 (2024-11-12)

Full Changelog: [v1.38.0...v1.39.0](https://github.com/julep-ai/python-sdk/compare/v1.38.0...v1.39.0)

### Features

* **api:** api update ([#157](https://github.com/julep-ai/python-sdk/issues/157)) ([56fd25e](https://github.com/julep-ai/python-sdk/commit/56fd25e60374a1c1da008903bb7bac33e93db7ba))

## 1.38.0 (2024-11-12)

Full Changelog: [v1.37.0...v1.38.0](https://github.com/julep-ai/python-sdk/compare/v1.37.0...v1.38.0)

### Features

* **api:** api update ([#154](https://github.com/julep-ai/python-sdk/issues/154)) ([5bd9f1e](https://github.com/julep-ai/python-sdk/commit/5bd9f1ead8e86b0d3ff555ba8e8ec249c8acc6ce))

## 1.37.0 (2024-11-11)

Full Changelog: [v1.36.0...v1.37.0](https://github.com/julep-ai/python-sdk/compare/v1.36.0...v1.37.0)

### Features

* **api:** api update ([#151](https://github.com/julep-ai/python-sdk/issues/151)) ([35f7878](https://github.com/julep-ai/python-sdk/commit/35f7878ce0f1c10fcd0c8c684c82dd556ef42581))

## 1.36.0 (2024-11-10)

Full Changelog: [v1.35.0...v1.36.0](https://github.com/julep-ai/python-sdk/compare/v1.35.0...v1.36.0)

### Features

* **api:** api update ([#148](https://github.com/julep-ai/python-sdk/issues/148)) ([bc1c1a1](https://github.com/julep-ai/python-sdk/commit/bc1c1a16cdc49793ca958978becf5104eef7f866))

## 1.35.0 (2024-11-09)

Full Changelog: [v1.34.0...v1.35.0](https://github.com/julep-ai/python-sdk/compare/v1.34.0...v1.35.0)

### Features

* **api:** api update ([#145](https://github.com/julep-ai/python-sdk/issues/145)) ([ab3d3d2](https://github.com/julep-ai/python-sdk/commit/ab3d3d2ddd351bebd3453bbf12acd44974a1a661))

## 1.34.0 (2024-11-09)

Full Changelog: [v1.33.0...v1.34.0](https://github.com/julep-ai/python-sdk/compare/v1.33.0...v1.34.0)

### Features

* **api:** api update ([#142](https://github.com/julep-ai/python-sdk/issues/142)) ([d3563f2](https://github.com/julep-ai/python-sdk/commit/d3563f2b712eaeeece097ef66f13b171fd10d044))

## 1.33.0 (2024-11-07)

Full Changelog: [v1.32.0...v1.33.0](https://github.com/julep-ai/python-sdk/compare/v1.32.0...v1.33.0)

### Features

* **api:** add custom api key; change uuid4 to uuid ([#8](https://github.com/julep-ai/python-sdk/issues/8)) ([cd7c76f](https://github.com/julep-ai/python-sdk/commit/cd7c76f817f3e69897bda62e2695a2e5ccfd5a8f))
* **api:** api update ([#100](https://github.com/julep-ai/python-sdk/issues/100)) ([4db7881](https://github.com/julep-ai/python-sdk/commit/4db7881d5add7cbd936d22a828ff1de9a0c57262))
* **api:** api update ([#103](https://github.com/julep-ai/python-sdk/issues/103)) ([01dbb00](https://github.com/julep-ai/python-sdk/commit/01dbb00fe174f518a4df80e4a2c02c7f6bba02d9))
* **api:** api update ([#109](https://github.com/julep-ai/python-sdk/issues/109)) ([ba242c8](https://github.com/julep-ai/python-sdk/commit/ba242c8aedc6c68d0c9dc3485a82afc86626255b))
* **api:** api update ([#112](https://github.com/julep-ai/python-sdk/issues/112)) ([8246545](https://github.com/julep-ai/python-sdk/commit/824654586047a2ad10420ef54545adea5ecfe345))
* **api:** api update ([#116](https://github.com/julep-ai/python-sdk/issues/116)) ([9c81e90](https://github.com/julep-ai/python-sdk/commit/9c81e90e0adf094ea5648311b1fe59f5c1400d76))
* **api:** api update ([#119](https://github.com/julep-ai/python-sdk/issues/119)) ([3bb1c3a](https://github.com/julep-ai/python-sdk/commit/3bb1c3a90b1a0018f621ff0360e13713d838e918))
* **api:** api update ([#122](https://github.com/julep-ai/python-sdk/issues/122)) ([f9096c6](https://github.com/julep-ai/python-sdk/commit/f9096c62b5b86a9673f0298e28a27d5a523eb656))
* **api:** api update ([#135](https://github.com/julep-ai/python-sdk/issues/135)) ([a1794d8](https://github.com/julep-ai/python-sdk/commit/a1794d8a8fc3397c61927b8e3a762fba49c0b9ac))
* **api:** api update ([#75](https://github.com/julep-ai/python-sdk/issues/75)) ([f3ebc89](https://github.com/julep-ai/python-sdk/commit/f3ebc891876b39d7fb564560e1d347c9c8e39810))
* **api:** api update ([#79](https://github.com/julep-ai/python-sdk/issues/79)) ([db5ea21](https://github.com/julep-ai/python-sdk/commit/db5ea21698fc85b67d20eafd64ea96df92ea4f55))
* **api:** api update ([#84](https://github.com/julep-ai/python-sdk/issues/84)) ([4343377](https://github.com/julep-ai/python-sdk/commit/43433776948eb4a3c44fbb6e746ea44489c16aab))
* **api:** api update ([#87](https://github.com/julep-ai/python-sdk/issues/87)) ([170e31a](https://github.com/julep-ai/python-sdk/commit/170e31ae2670755e80578a4b19551e80265bd7d0))
* **api:** api update ([#90](https://github.com/julep-ai/python-sdk/issues/90)) ([b534787](https://github.com/julep-ai/python-sdk/commit/b534787d0b4e32c53a9f0ab5b14b2693f151973e))
* **api:** api update ([#94](https://github.com/julep-ai/python-sdk/issues/94)) ([5e1764d](https://github.com/julep-ai/python-sdk/commit/5e1764db94e0a713b0ef14ac8e0b6d8f0957fb04))
* **api:** api update ([#97](https://github.com/julep-ai/python-sdk/issues/97)) ([38b7218](https://github.com/julep-ai/python-sdk/commit/38b721831e96e125a532fb69911ab9588d751435))
* **api:** manual change nested_format-&gt;dots and array_format->repeat in query settings ([#52](https://github.com/julep-ai/python-sdk/issues/52)) ([22ffd50](https://github.com/julep-ai/python-sdk/commit/22ffd50bd6f027c01c972a5aafd0f7b39e1bd836))
* **api:** OpenAPI spec update via Stainless API ([#19](https://github.com/julep-ai/python-sdk/issues/19)) ([c27c232](https://github.com/julep-ai/python-sdk/commit/c27c232a662f936c8f28ae32d9e19fddca2f6ccd))
* **api:** OpenAPI spec update via Stainless API ([#20](https://github.com/julep-ai/python-sdk/issues/20)) ([d8ff0e5](https://github.com/julep-ai/python-sdk/commit/d8ff0e5d14cee458d3f853491df93da0f0a34fc5))
* **api:** OpenAPI spec update via Stainless API ([#29](https://github.com/julep-ai/python-sdk/issues/29)) ([daf84a2](https://github.com/julep-ai/python-sdk/commit/daf84a2290023007673baceec2b3f7d8f6bb9af6))
* **api:** OpenAPI spec update via Stainless API ([#32](https://github.com/julep-ai/python-sdk/issues/32)) ([e082886](https://github.com/julep-ai/python-sdk/commit/e0828868c9a0e22bc2aab884704857d80627956d))
* **api:** OpenAPI spec update via Stainless API ([#35](https://github.com/julep-ai/python-sdk/issues/35)) ([0601eac](https://github.com/julep-ai/python-sdk/commit/0601eac834ad0a694e203ab3083dfade28bd92cb))
* **api:** OpenAPI spec update via Stainless API ([#41](https://github.com/julep-ai/python-sdk/issues/41)) ([bf50065](https://github.com/julep-ai/python-sdk/commit/bf500659b46812ec2fed862db604bc5e8d9be0ab))
* **api:** OpenAPI spec update via Stainless API ([#43](https://github.com/julep-ai/python-sdk/issues/43)) ([c9f285c](https://github.com/julep-ai/python-sdk/commit/c9f285cde7718ab346c6a035dfaa7b5921fdc178))
* **api:** OpenAPI spec update via Stainless API ([#46](https://github.com/julep-ai/python-sdk/issues/46)) ([a1501ef](https://github.com/julep-ai/python-sdk/commit/a1501ef05661aa9dfc967c54ba89f20a9e2ceecf))
* **api:** OpenAPI spec update via Stainless API ([#49](https://github.com/julep-ai/python-sdk/issues/49)) ([3bb6222](https://github.com/julep-ai/python-sdk/commit/3bb6222a912376625ccd4325c1a17a5a8a30d93b))
* **api:** OpenAPI spec update via Stainless API ([#5](https://github.com/julep-ai/python-sdk/issues/5)) ([9b26042](https://github.com/julep-ai/python-sdk/commit/9b26042873376b09db3f51e66a18118ecca8d69a))
* **api:** OpenAPI spec update via Stainless API ([#57](https://github.com/julep-ai/python-sdk/issues/57)) ([cae5425](https://github.com/julep-ai/python-sdk/commit/cae54258b8a7c46ce9b1478f01d278f0c6f5c019))
* **api:** OpenAPI spec update via Stainless API ([#60](https://github.com/julep-ai/python-sdk/issues/60)) ([5ed1a8d](https://github.com/julep-ai/python-sdk/commit/5ed1a8db473d1de7c95a55742e3aef64d08fe073))
* **api:** OpenAPI spec update via Stainless API ([#63](https://github.com/julep-ai/python-sdk/issues/63)) ([9d97c44](https://github.com/julep-ai/python-sdk/commit/9d97c444de06130719827c93e3b14cd42728e2cd))
* **api:** OpenAPI spec update via Stainless API ([#66](https://github.com/julep-ai/python-sdk/issues/66)) ([26079cb](https://github.com/julep-ai/python-sdk/commit/26079cb9bd7de3b9ba67de5860582410ec03c27b))
* **api:** update via SDK Studio ([99fc2a4](https://github.com/julep-ai/python-sdk/commit/99fc2a47f868f50591c92614a73a57a4604de0ac))
* **api:** update via SDK Studio ([d4c5ba9](https://github.com/julep-ai/python-sdk/commit/d4c5ba9ffd8776d50fd18d187794526459fddad2))
* **api:** update via SDK Studio ([d681e89](https://github.com/julep-ai/python-sdk/commit/d681e89770f3b96bc44549a4d808aaeed8d160bf))
* **api:** update via SDK Studio ([73e713c](https://github.com/julep-ai/python-sdk/commit/73e713c728dd81128b94a15eb258821c30130a50))
* **api:** update via SDK Studio ([4e9f83d](https://github.com/julep-ai/python-sdk/commit/4e9f83d59a40271d00cc546afa5496e779ed90a3))
* **api:** update via SDK Studio ([8f60449](https://github.com/julep-ai/python-sdk/commit/8f60449dc1ffe285142118e185da8517c6468667))
* **api:** update via SDK Studio ([dda74e1](https://github.com/julep-ai/python-sdk/commit/dda74e10af0fff634ceaccfb8c7eb7b0f705226a))
* **api:** update via SDK Studio ([e8c3b6f](https://github.com/julep-ai/python-sdk/commit/e8c3b6fcc486eab93bc48e442303381849128601))
* **api:** update via SDK Studio ([d287c9f](https://github.com/julep-ai/python-sdk/commit/d287c9fab4dca657672d3c4495fb2c6ef37508f3))
* **api:** update via SDK Studio ([e7b85a3](https://github.com/julep-ai/python-sdk/commit/e7b85a3e0a5f1206d65a19544a74378a04987b00))
* **api:** update via SDK Studio ([949a676](https://github.com/julep-ai/python-sdk/commit/949a676bb310f28fff7806d39e8e254cb135b75d))
* **api:** update via SDK Studio ([281bafd](https://github.com/julep-ai/python-sdk/commit/281bafd01d7a9c8a3e2f3a3f57fd0e647f7d5ca5))
* **client:** send retry count header ([#17](https://github.com/julep-ai/python-sdk/issues/17)) ([8f99506](https://github.com/julep-ai/python-sdk/commit/8f995066384e390b1a1a4e514c4493702a2145d0))
* deps: Add dotenv as a bundled dep ([08fd755](https://github.com/julep-ai/python-sdk/commit/08fd7557f1bd334a2be302090bdfb3545e18d540))
* various codegen changes ([779a7e3](https://github.com/julep-ai/python-sdk/commit/779a7e3682819e8e7a83f0ddaf9052d62c280fb6))


### Bug Fixes

* **client:** avoid OverflowError with very large retry counts ([#69](https://github.com/julep-ai/python-sdk/issues/69)) ([67375a3](https://github.com/julep-ai/python-sdk/commit/67375a31c5c773e1fb01152ac5d6120965c1a1ce))
* **client:** handle domains with underscores ([#15](https://github.com/julep-ai/python-sdk/issues/15)) ([eb905a1](https://github.com/julep-ai/python-sdk/commit/eb905a138dfc235308b630268efd14132daa2774))
* Extend create and create_or_update methods for tasks ([be6ac8e](https://github.com/julep-ai/python-sdk/commit/be6ac8e133b7456bc167c158323da0edb74cdd1d))
* Fix import ([405e1db](https://github.com/julep-ai/python-sdk/commit/405e1dba578da2732373431bbae0e4b802554699))
* Fix positional args handling ([fdb1d64](https://github.com/julep-ai/python-sdk/commit/fdb1d642376caab9dd59e00621a5fce2a042dad0))
* **lib:** Fix inspect args logic ([cbe409c](https://github.com/julep-ai/python-sdk/commit/cbe409cb7f33ad0b5cd17e8a59c1f491146007ae))
* Pop extra args from argument list ([b2133aa](https://github.com/julep-ai/python-sdk/commit/b2133aa4f9df8b825c3ad8dda2b78f4ff1e93a1a))
* remove unused import ([a5c7b48](https://github.com/julep-ai/python-sdk/commit/a5c7b48b155ea4231a16ac8f7b74b8eb0b8e2feb))


### Chores

* add repr to PageInfo class ([#72](https://github.com/julep-ai/python-sdk/issues/72)) ([4b1d049](https://github.com/julep-ai/python-sdk/commit/4b1d0497ed765df25e1c401a6b414fd58a32223c))
* Fix formatting ([a0b10ef](https://github.com/julep-ai/python-sdk/commit/a0b10ef5b42e43dd15a4de7a2f5e642efa23cc84))
* go live ([#1](https://github.com/julep-ai/python-sdk/issues/1)) ([f720320](https://github.com/julep-ai/python-sdk/commit/f720320217bf4d1935c6270627510dc6329c1df7))
* Ignore attr defined error ([abd8afe](https://github.com/julep-ai/python-sdk/commit/abd8afe890a22a79ee718363d1ab61ed863ab0cb))
* Ignore typing errors ([3de90b1](https://github.com/julep-ai/python-sdk/commit/3de90b100ad1f99c3824bde44699651f22ff7a33))
* **internal:** add support for parsing bool response content ([#54](https://github.com/julep-ai/python-sdk/issues/54)) ([fb290f2](https://github.com/julep-ai/python-sdk/commit/fb290f2119eb9ff66549d1c360b89d8dcb35d92d))
* **internal:** bump pyright / mypy version ([#14](https://github.com/julep-ai/python-sdk/issues/14)) ([e6e180d](https://github.com/julep-ai/python-sdk/commit/e6e180d070a9606268aa42dacfa9fb220bfa57ec))
* **internal:** codegen changes ([#132](https://github.com/julep-ai/python-sdk/issues/132)) ([788174f](https://github.com/julep-ai/python-sdk/commit/788174f87532023544abdda7d78ce67209212069))
* **internal:** codegen related update ([#12](https://github.com/julep-ai/python-sdk/issues/12)) ([8c12efc](https://github.com/julep-ai/python-sdk/commit/8c12efc5d10b0ce84bc760158025b7a34d6fd1fc))
* **internal:** codegen related update ([#27](https://github.com/julep-ai/python-sdk/issues/27)) ([cb98d42](https://github.com/julep-ai/python-sdk/commit/cb98d423b87043de48ca3e845f107b797a69824b))
* **internal:** codegen related update ([#38](https://github.com/julep-ai/python-sdk/issues/38)) ([03c8e84](https://github.com/julep-ai/python-sdk/commit/03c8e84ed43a97c943642703eedaa230166fb055))
* **internal:** codegen related update ([#40](https://github.com/julep-ai/python-sdk/issues/40)) ([d64f86a](https://github.com/julep-ai/python-sdk/commit/d64f86a1b7a47ed0ec53af42f2bf96b4718fc80d))
* **internal:** update pydantic v1 compat helpers ([#22](https://github.com/julep-ai/python-sdk/issues/22)) ([f90bc17](https://github.com/julep-ai/python-sdk/commit/f90bc1783cee6669055f02fe9621f5b70a2f5d89))
* **internal:** use `typing_extensions.overload` instead of `typing` ([#25](https://github.com/julep-ai/python-sdk/issues/25)) ([3c50f29](https://github.com/julep-ai/python-sdk/commit/3c50f297ee48e3a7bc284551a1cd12905bc7ae29))
* rebuild project due to codegen change ([#137](https://github.com/julep-ai/python-sdk/issues/137)) ([70a972d](https://github.com/julep-ai/python-sdk/commit/70a972df3336dc9ebfbd885ee0b80d1e9d4550a6))
* update SDK settings ([#3](https://github.com/julep-ai/python-sdk/issues/3)) ([a603b61](https://github.com/julep-ai/python-sdk/commit/a603b61b57b910e77c602feaf93f9f18bf722a95))

## 1.32.0 (2024-11-07)

Full Changelog: [v1.31.1...v1.32.0](https://github.com/julep-ai/python-sdk/compare/v1.31.1...v1.32.0)

### Features

* **api:** api update ([#135](https://github.com/julep-ai/python-sdk/issues/135)) ([b254016](https://github.com/julep-ai/python-sdk/commit/b254016b177acfb74c8618d4f687163aac59ec4e))

## 1.31.1 (2024-11-02)

Full Changelog: [v1.31.0...v1.31.1](https://github.com/julep-ai/python-sdk/compare/v1.31.0...v1.31.1)

### Bug Fixes

* remove unused import ([cc74aa2](https://github.com/julep-ai/python-sdk/commit/cc74aa29c6030b6e1e6f3922d1cb7342cdedd8c5))


### Chores

* **internal:** codegen changes ([#132](https://github.com/julep-ai/python-sdk/issues/132)) ([bb9600c](https://github.com/julep-ai/python-sdk/commit/bb9600cc75daebccf207b23e0dd8db8bfb9cfef7))

## 1.31.0 (2024-11-02)

Full Changelog: [v1.30.0...v1.31.0](https://github.com/julep-ai/python-sdk/compare/v1.30.0...v1.31.0)

### Features

* various codegen changes ([cdb714e](https://github.com/julep-ai/python-sdk/commit/cdb714e443fbdb6caf9f8a612adfeae21d7e1b2a))


### Bug Fixes

* **lib:** Fix inspect args logic ([cbe409c](https://github.com/julep-ai/python-sdk/commit/cbe409cb7f33ad0b5cd17e8a59c1f491146007ae))

## 1.30.0 (2024-11-01)

Full Changelog: [v1.29.0...v1.30.0](https://github.com/julep-ai/python-sdk/compare/v1.29.0...v1.30.0)

### Features

* **api:** api update ([#122](https://github.com/julep-ai/python-sdk/issues/122)) ([bd300dc](https://github.com/julep-ai/python-sdk/commit/bd300dcb1c2e03b245a5fd7795b5fd64732555fa))
* Update __init__.py ([ab075ee](https://github.com/julep-ai/python-sdk/commit/ab075ee89466bdd2848ac6431b0d2a7829a00e3e))

## 1.29.0 (2024-11-01)

Full Changelog: [v1.28.0...v1.29.0](https://github.com/julep-ai/python-sdk/compare/v1.28.0...v1.29.0)

### Features

* **api:** api update ([#119](https://github.com/julep-ai/python-sdk/issues/119)) ([05c25ee](https://github.com/julep-ai/python-sdk/commit/05c25ee9df8c4b87f40a40285c2b18662fd82104))

## 1.28.0 (2024-10-31)

Full Changelog: [v1.27.0...v1.28.0](https://github.com/julep-ai/python-sdk/compare/v1.27.0...v1.28.0)

### Features

* **api:** api update ([#116](https://github.com/julep-ai/python-sdk/issues/116)) ([25b96db](https://github.com/julep-ai/python-sdk/commit/25b96db8eafee879d7da26f07cb2666c44a1d02e))

## 1.27.0 (2024-10-31)

Full Changelog: [v1.26.0...v1.27.0](https://github.com/julep-ai/python-sdk/compare/v1.26.0...v1.27.0)

### Features

* **api:** api update ([#112](https://github.com/julep-ai/python-sdk/issues/112)) ([d9c4b22](https://github.com/julep-ai/python-sdk/commit/d9c4b22022ee8fdf43cc080e700635ff4bd0d180))

## 1.26.0 (2024-10-30)

Full Changelog: [v1.25.1...v1.26.0](https://github.com/julep-ai/python-sdk/compare/v1.25.1...v1.26.0)

### Features

* **api:** api update ([#109](https://github.com/julep-ai/python-sdk/issues/109)) ([a6fbe4c](https://github.com/julep-ai/python-sdk/commit/a6fbe4c0cd2c250d2b2fee3454a9aee7cfa78ac8))

## 1.25.1 (2024-10-30)

Full Changelog: [v1.25.0...v1.25.1](https://github.com/julep-ai/python-sdk/compare/v1.25.0...v1.25.1)

### Bug Fixes

* Fix import ([405e1db](https://github.com/julep-ai/python-sdk/commit/405e1dba578da2732373431bbae0e4b802554699))


### Chores

* Fix formatting ([a0b10ef](https://github.com/julep-ai/python-sdk/commit/a0b10ef5b42e43dd15a4de7a2f5e642efa23cc84))
* Ignore attr defined error ([abd8afe](https://github.com/julep-ai/python-sdk/commit/abd8afe890a22a79ee718363d1ab61ed863ab0cb))
* Ignore typing errors ([3de90b1](https://github.com/julep-ai/python-sdk/commit/3de90b100ad1f99c3824bde44699651f22ff7a33))

## 1.25.0 (2024-10-30)

Full Changelog: [v1.24.0...v1.25.0](https://github.com/julep-ai/python-sdk/compare/v1.24.0...v1.25.0)

### Features

* **api:** api update ([#103](https://github.com/julep-ai/python-sdk/issues/103)) ([7bebd2c](https://github.com/julep-ai/python-sdk/commit/7bebd2c9252b476821df1704ae636d8e88c70d77))

## 1.24.0 (2024-10-29)

Full Changelog: [v1.23.0...v1.24.0](https://github.com/julep-ai/python-sdk/compare/v1.23.0...v1.24.0)

### Features

* **api:** api update ([#100](https://github.com/julep-ai/python-sdk/issues/100)) ([0797355](https://github.com/julep-ai/python-sdk/commit/0797355a735592816b671d6fcadcc74f2bc51f6f))

## 1.23.0 (2024-10-29)

Full Changelog: [v1.22.0...v1.23.0](https://github.com/julep-ai/python-sdk/compare/v1.22.0...v1.23.0)

### Features

* **api:** api update ([#97](https://github.com/julep-ai/python-sdk/issues/97)) ([0ce9e8a](https://github.com/julep-ai/python-sdk/commit/0ce9e8a02d536ded730984148c834606c2ba0885))

## 1.22.0 (2024-10-29)

Full Changelog: [v1.21.0...v1.22.0](https://github.com/julep-ai/python-sdk/compare/v1.21.0...v1.22.0)

### Features

* **api:** api update ([#94](https://github.com/julep-ai/python-sdk/issues/94)) ([34965df](https://github.com/julep-ai/python-sdk/commit/34965df8e42611263e5dc7b05ab2d69fad917dd1))

## 1.21.0 (2024-10-26)

Full Changelog: [v1.20.0...v1.21.0](https://github.com/julep-ai/python-sdk/compare/v1.20.0...v1.21.0)

### Features

* **api:** api update ([#90](https://github.com/julep-ai/python-sdk/issues/90)) ([ee0e9f3](https://github.com/julep-ai/python-sdk/commit/ee0e9f3edae1941e4d25d64e5473604624635b77))

## 1.20.0 (2024-10-22)

Full Changelog: [v1.19.0...v1.20.0](https://github.com/julep-ai/python-sdk/compare/v1.19.0...v1.20.0)

### Features

* **api:** api update ([#87](https://github.com/julep-ai/python-sdk/issues/87)) ([d527d77](https://github.com/julep-ai/python-sdk/commit/d527d775ceafdc68a4464e0def71453c161ad00b))

## 1.19.0 (2024-10-19)

Full Changelog: [v1.18.0...v1.19.0](https://github.com/julep-ai/python-sdk/compare/v1.18.0...v1.19.0)

### Features

* **api:** api update ([#84](https://github.com/julep-ai/python-sdk/issues/84)) ([6e33e65](https://github.com/julep-ai/python-sdk/commit/6e33e65fd81c9c4dd3848e505fe02f0cc5775b34))

## 1.18.0 (2024-10-18)

Full Changelog: [v1.17.0...v1.18.0](https://github.com/julep-ai/python-sdk/compare/v1.17.0...v1.18.0)

### Features

* deps: Add dotenv as a bundled dep ([08fd755](https://github.com/julep-ai/python-sdk/commit/08fd7557f1bd334a2be302090bdfb3545e18d540))

## 1.17.0 (2024-10-18)

Full Changelog: [v1.16.0...v1.17.0](https://github.com/julep-ai/python-sdk/compare/v1.16.0...v1.17.0)

### Features

* **api:** api update ([#79](https://github.com/julep-ai/python-sdk/issues/79)) ([50f22a4](https://github.com/julep-ai/python-sdk/commit/50f22a49c7c9d12f7315236803832340aacf1029))

## 1.16.0 (2024-10-10)

Full Changelog: [v1.15.2...v1.16.0](https://github.com/julep-ai/python-sdk/compare/v1.15.2...v1.16.0)

### Features

* **api:** api update ([#75](https://github.com/julep-ai/python-sdk/issues/75)) ([6db4387](https://github.com/julep-ai/python-sdk/commit/6db4387c664a099f45c0ac8d716767060bbc8732))

## 1.15.2 (2024-10-07)

Full Changelog: [v1.15.1...v1.15.2](https://github.com/julep-ai/python-sdk/compare/v1.15.1...v1.15.2)

### Chores

* add repr to PageInfo class ([#72](https://github.com/julep-ai/python-sdk/issues/72)) ([4b1d049](https://github.com/julep-ai/python-sdk/commit/4b1d0497ed765df25e1c401a6b414fd58a32223c))

## 1.15.1 (2024-10-07)

Full Changelog: [v1.15.0...v1.15.1](https://github.com/julep-ai/python-sdk/compare/v1.15.0...v1.15.1)

### Bug Fixes

* **client:** avoid OverflowError with very large retry counts ([#69](https://github.com/julep-ai/python-sdk/issues/69)) ([7e9c5de](https://github.com/julep-ai/python-sdk/commit/7e9c5ded74f129cdb0cbb84c804c8e892c22fe8b))

## 1.15.0 (2024-10-07)

Full Changelog: [v1.14.0...v1.15.0](https://github.com/julep-ai/python-sdk/compare/v1.14.0...v1.15.0)

### Features

* **api:** OpenAPI spec update via Stainless API ([#66](https://github.com/julep-ai/python-sdk/issues/66)) ([cfc33cc](https://github.com/julep-ai/python-sdk/commit/cfc33ccd90a18cce8539c8bd3398e90505b45934))

## 1.14.0 (2024-10-05)

Full Changelog: [v1.13.0...v1.14.0](https://github.com/julep-ai/python-sdk/compare/v1.13.0...v1.14.0)

### Features

* **api:** OpenAPI spec update via Stainless API ([#63](https://github.com/julep-ai/python-sdk/issues/63)) ([fbd636d](https://github.com/julep-ai/python-sdk/commit/fbd636d3c2962f2e8ad8f927ba604c13df62423a))

## 1.13.0 (2024-10-05)

Full Changelog: [v1.12.0...v1.13.0](https://github.com/julep-ai/python-sdk/compare/v1.12.0...v1.13.0)

### Features

* **api:** OpenAPI spec update via Stainless API ([#60](https://github.com/julep-ai/python-sdk/issues/60)) ([1bb231a](https://github.com/julep-ai/python-sdk/commit/1bb231a3dc7e5012c241cf3a83829e8fbbcf4cec))

## 1.12.0 (2024-10-05)

Full Changelog: [v1.11.1...v1.12.0](https://github.com/julep-ai/python-sdk/compare/v1.11.1...v1.12.0)

### Features

* **api:** OpenAPI spec update via Stainless API ([#57](https://github.com/julep-ai/python-sdk/issues/57)) ([d2a2f6f](https://github.com/julep-ai/python-sdk/commit/d2a2f6f2cdae0599e06b6772ef7176948bb18dcc))

## 1.11.1 (2024-10-04)

Full Changelog: [v1.11.0...v1.11.1](https://github.com/julep-ai/python-sdk/compare/v1.11.0...v1.11.1)

### Chores

* **internal:** add support for parsing bool response content ([#54](https://github.com/julep-ai/python-sdk/issues/54)) ([fb290f2](https://github.com/julep-ai/python-sdk/commit/fb290f2119eb9ff66549d1c360b89d8dcb35d92d))

## 1.11.0 (2024-10-04)

Full Changelog: [v1.10.0...v1.11.0](https://github.com/julep-ai/python-sdk/compare/v1.10.0...v1.11.0)

### Features

* **api:** manual change nested_format-&gt;dots and array_format->repeat in query settings ([#52](https://github.com/julep-ai/python-sdk/issues/52)) ([51c5ad8](https://github.com/julep-ai/python-sdk/commit/51c5ad8fa7a9a31e3d1d5ace3b7e052c1f22b589))

## 1.10.0 (2024-10-04)

Full Changelog: [v1.9.0...v1.10.0](https://github.com/julep-ai/python-sdk/compare/v1.9.0...v1.10.0)

### Features

* **api:** OpenAPI spec update via Stainless API ([#49](https://github.com/julep-ai/python-sdk/issues/49)) ([7e6100c](https://github.com/julep-ai/python-sdk/commit/7e6100c26e9189a6f7d8db0ab003b5aa3cd20412))

## 1.9.0 (2024-10-04)

Full Changelog: [v1.8.0...v1.9.0](https://github.com/julep-ai/python-sdk/compare/v1.8.0...v1.9.0)

### Features

* **api:** OpenAPI spec update via Stainless API ([#46](https://github.com/julep-ai/python-sdk/issues/46)) ([9ec3586](https://github.com/julep-ai/python-sdk/commit/9ec358673c6294b10b795a79659b315f12ec3043))

## 1.8.0 (2024-10-03)

Full Changelog: [v1.7.0...v1.8.0](https://github.com/julep-ai/python-sdk/compare/v1.7.0...v1.8.0)

### Features

* **api:** OpenAPI spec update via Stainless API ([#43](https://github.com/julep-ai/python-sdk/issues/43)) ([584193e](https://github.com/julep-ai/python-sdk/commit/584193ee4cb0c8162f34a31377605685f74a2ab8))

## 1.7.0 (2024-10-02)

Full Changelog: [v1.6.0...v1.7.0](https://github.com/julep-ai/python-sdk/compare/v1.6.0...v1.7.0)

### Features

* **api:** OpenAPI spec update via Stainless API ([#41](https://github.com/julep-ai/python-sdk/issues/41)) ([917f242](https://github.com/julep-ai/python-sdk/commit/917f2426867ce8596f3e95803434c554c7da6cca))


### Chores

* **internal:** codegen related update ([#38](https://github.com/julep-ai/python-sdk/issues/38)) ([09aee2a](https://github.com/julep-ai/python-sdk/commit/09aee2a3e59cbbb932cfe459bda1cb28614d9803))
* **internal:** codegen related update ([#40](https://github.com/julep-ai/python-sdk/issues/40)) ([4d768b7](https://github.com/julep-ai/python-sdk/commit/4d768b75e0361f8a8a0edd690511f8c4410b88f7))

## 1.6.0 (2024-10-01)

Full Changelog: [v1.5.0...v1.6.0](https://github.com/julep-ai/python-sdk/compare/v1.5.0...v1.6.0)

### Features

* **api:** OpenAPI spec update via Stainless API ([#35](https://github.com/julep-ai/python-sdk/issues/35)) ([316651d](https://github.com/julep-ai/python-sdk/commit/316651db98a3bc64dd6a236acb0ab6064f65bbaf))

## 1.5.0 (2024-09-25)

Full Changelog: [v1.4.0...v1.5.0](https://github.com/julep-ai/python-sdk/compare/v1.4.0...v1.5.0)

### Features

* **api:** OpenAPI spec update via Stainless API ([#32](https://github.com/julep-ai/python-sdk/issues/32)) ([f359535](https://github.com/julep-ai/python-sdk/commit/f3595355079ad286913b6ac8516f98220c6cb8a4))

## 1.4.0 (2024-09-25)

Full Changelog: [v1.3.2...v1.4.0](https://github.com/julep-ai/python-sdk/compare/v1.3.2...v1.4.0)

### Features

* **api:** OpenAPI spec update via Stainless API ([#29](https://github.com/julep-ai/python-sdk/issues/29)) ([4223a5c](https://github.com/julep-ai/python-sdk/commit/4223a5c207e93acc0ede043b76d3dbc0e731e7a7))

## 1.3.2 (2024-09-25)

Full Changelog: [v1.3.1...v1.3.2](https://github.com/julep-ai/python-sdk/compare/v1.3.1...v1.3.2)

### Chores

* **internal:** codegen related update ([#27](https://github.com/julep-ai/python-sdk/issues/27)) ([cb98d42](https://github.com/julep-ai/python-sdk/commit/cb98d423b87043de48ca3e845f107b797a69824b))
* **internal:** use `typing_extensions.overload` instead of `typing` ([#25](https://github.com/julep-ai/python-sdk/issues/25)) ([3c50f29](https://github.com/julep-ai/python-sdk/commit/3c50f297ee48e3a7bc284551a1cd12905bc7ae29))

## 1.3.1 (2024-09-24)

Full Changelog: [v1.3.0...v1.3.1](https://github.com/julep-ai/python-sdk/compare/v1.3.0...v1.3.1)

### Chores

* **internal:** update pydantic v1 compat helpers ([#22](https://github.com/julep-ai/python-sdk/issues/22)) ([f90bc17](https://github.com/julep-ai/python-sdk/commit/f90bc1783cee6669055f02fe9621f5b70a2f5d89))

## 1.3.0 (2024-09-23)

Full Changelog: [v1.2.1...v1.3.0](https://github.com/julep-ai/python-sdk/compare/v1.2.1...v1.3.0)

### Features

* **api:** OpenAPI spec update via Stainless API ([#19](https://github.com/julep-ai/python-sdk/issues/19)) ([c27c232](https://github.com/julep-ai/python-sdk/commit/c27c232a662f936c8f28ae32d9e19fddca2f6ccd))
* **api:** OpenAPI spec update via Stainless API ([#20](https://github.com/julep-ai/python-sdk/issues/20)) ([d8ff0e5](https://github.com/julep-ai/python-sdk/commit/d8ff0e5d14cee458d3f853491df93da0f0a34fc5))
* **client:** send retry count header ([#17](https://github.com/julep-ai/python-sdk/issues/17)) ([8f99506](https://github.com/julep-ai/python-sdk/commit/8f995066384e390b1a1a4e514c4493702a2145d0))

## 1.2.1 (2024-09-19)

Full Changelog: [v1.2.0...v1.2.1](https://github.com/julep-ai/python-sdk/compare/v1.2.0...v1.2.1)

### Bug Fixes

* **client:** handle domains with underscores ([#15](https://github.com/julep-ai/python-sdk/issues/15)) ([f00026b](https://github.com/julep-ai/python-sdk/commit/f00026bf6cd9360eab7620d145add2616b4d3702))


### Chores

* **internal:** bump pyright / mypy version ([#14](https://github.com/julep-ai/python-sdk/issues/14)) ([73a4b15](https://github.com/julep-ai/python-sdk/commit/73a4b151a593dfa38523586d3511ee5ebfc663f1))
* **internal:** codegen related update ([#12](https://github.com/julep-ai/python-sdk/issues/12)) ([4309b50](https://github.com/julep-ai/python-sdk/commit/4309b50db10f755f0d57a8638b97356058e4d93e))

## 1.2.0 (2024-09-19)

Full Changelog: [v1.1.0...v1.2.0](https://github.com/julep-ai/python-sdk/compare/v1.1.0...v1.2.0)

### Features

* **api:** add custom api key; change uuid4 to uuid ([#8](https://github.com/julep-ai/python-sdk/issues/8)) ([7b2488e](https://github.com/julep-ai/python-sdk/commit/7b2488e990dea41628541cb9311a802d5f7ba884))

## 1.1.0 (2024-09-13)

Full Changelog: [v1.0.1...v1.1.0](https://github.com/julep-ai/python-sdk/compare/v1.0.1...v1.1.0)

### Features

* **api:** OpenAPI spec update via Stainless API ([#5](https://github.com/julep-ai/python-sdk/issues/5)) ([9b26042](https://github.com/julep-ai/python-sdk/commit/9b26042873376b09db3f51e66a18118ecca8d69a))

## 1.0.1 (2024-09-13)

Full Changelog: [v0.0.1-alpha.0...v1.0.1](https://github.com/julep-ai/python-sdk/compare/v0.0.1-alpha.0...v1.0.1)

### Features

* **api:** update via SDK Studio ([99fc2a4](https://github.com/julep-ai/python-sdk/commit/99fc2a47f868f50591c92614a73a57a4604de0ac))
* **api:** update via SDK Studio ([d4c5ba9](https://github.com/julep-ai/python-sdk/commit/d4c5ba9ffd8776d50fd18d187794526459fddad2))
* **api:** update via SDK Studio ([d681e89](https://github.com/julep-ai/python-sdk/commit/d681e89770f3b96bc44549a4d808aaeed8d160bf))
* **api:** update via SDK Studio ([73e713c](https://github.com/julep-ai/python-sdk/commit/73e713c728dd81128b94a15eb258821c30130a50))
* **api:** update via SDK Studio ([4e9f83d](https://github.com/julep-ai/python-sdk/commit/4e9f83d59a40271d00cc546afa5496e779ed90a3))
* **api:** update via SDK Studio ([8f60449](https://github.com/julep-ai/python-sdk/commit/8f60449dc1ffe285142118e185da8517c6468667))
* **api:** update via SDK Studio ([dda74e1](https://github.com/julep-ai/python-sdk/commit/dda74e10af0fff634ceaccfb8c7eb7b0f705226a))
* **api:** update via SDK Studio ([e8c3b6f](https://github.com/julep-ai/python-sdk/commit/e8c3b6fcc486eab93bc48e442303381849128601))
* **api:** update via SDK Studio ([d287c9f](https://github.com/julep-ai/python-sdk/commit/d287c9fab4dca657672d3c4495fb2c6ef37508f3))
* **api:** update via SDK Studio ([e7b85a3](https://github.com/julep-ai/python-sdk/commit/e7b85a3e0a5f1206d65a19544a74378a04987b00))
* **api:** update via SDK Studio ([949a676](https://github.com/julep-ai/python-sdk/commit/949a676bb310f28fff7806d39e8e254cb135b75d))
* **api:** update via SDK Studio ([281bafd](https://github.com/julep-ai/python-sdk/commit/281bafd01d7a9c8a3e2f3a3f57fd0e647f7d5ca5))


### Chores

* go live ([#1](https://github.com/julep-ai/python-sdk/issues/1)) ([f720320](https://github.com/julep-ai/python-sdk/commit/f720320217bf4d1935c6270627510dc6329c1df7))
* update SDK settings ([#3](https://github.com/julep-ai/python-sdk/issues/3)) ([a603b61](https://github.com/julep-ai/python-sdk/commit/a603b61b57b910e77c602feaf93f9f18bf722a95))
