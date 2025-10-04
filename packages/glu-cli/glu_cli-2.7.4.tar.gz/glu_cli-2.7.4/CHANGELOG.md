# Changelog

<!-- version list -->

## v2.7.4 (2025-10-04)

### Bug Fixes

- Switch default OpenAI model to gpt-5-mini to fix empty responses with o4-mini
  ([#61](https://github.com/BrightNight-Energy/glu/pull/61),
  [`8ef8cfb`](https://github.com/BrightNight-Energy/glu/commit/8ef8cfb6eed89c3848c861d57094c9cdd0e0b1d4))

- Validate commit type against conventional_commit_types.json
  ([#62](https://github.com/BrightNight-Energy/glu/pull/62),
  [`3a1cb0e`](https://github.com/BrightNight-Energy/glu/commit/3a1cb0ea841ed41009f65e997509a16906b27426))


## v2.7.3 (2025-09-25)

### Bug Fixes

- **commit-gen**: Fix double entry of type prefix in commit title when generating with AI
  ([#60](https://github.com/BrightNight-Energy/glu/pull/60),
  [`e3a956c`](https://github.com/BrightNight-Energy/glu/commit/e3a956c616330934647c013b08c1b45ea2d7f777))


## v2.7.2 (2025-09-16)

### Bug Fixes

- Upgrade jira package to fix endpoint depreciations
  ([#59](https://github.com/BrightNight-Energy/glu/pull/59),
  [`5456dad`](https://github.com/BrightNight-Energy/glu/commit/5456dad3e209289b3018c86fd373d0100a6d9061))


## v2.7.1 (2025-09-15)

### Bug Fixes

- Fix commit generation parsing when type is contained inside title
  ([#58](https://github.com/BrightNight-Energy/glu/pull/58),
  [`8d3033e`](https://github.com/BrightNight-Energy/glu/commit/8d3033ed4b3431602140c50020513c6431cd924b))

- Prioritize approved status over change requests in get_pr_approval_status
  ([#57](https://github.com/BrightNight-Energy/glu/pull/57),
  [`448ede9`](https://github.com/BrightNight-Energy/glu/commit/448ede90e27700331945b3876d8fbc78c987c4d1))


## v2.7.0 (2025-08-15)

### Features

- Added logic to set the upstream branch if unset
  ([#56](https://github.com/BrightNight-Energy/glu/pull/56),
  [`6f601bf`](https://github.com/BrightNight-Energy/glu/commit/6f601bf9e19febffc8a5ba84a18c000856d14d8d))


## v2.6.0 (2025-07-27)

### Chores

- Update README ([#54](https://github.com/BrightNight-Energy/glu/pull/54),
  [`39a5cd4`](https://github.com/BrightNight-Energy/glu/commit/39a5cd4a98ae0af1cb237532fc5361c699646e53))

### Features

- Cli(ticket): add search, assignee and reporter filters to list command
  ([#55](https://github.com/BrightNight-Energy/glu/pull/55),
  [`19cba06`](https://github.com/BrightNight-Energy/glu/commit/19cba060939b502c4a589cae7f9ae7862bdd4638))


## v2.5.0 (2025-07-20)

### Features

- Add `glu pr list` and `glu pr open` commands
  ([`42fe96f`](https://github.com/BrightNight-Energy/glu/commit/42fe96f3359a7ff218dc18b16c556753303433ba))

- Add `ticket list` command to list Jira tickets
  ([`9925ae2`](https://github.com/BrightNight-Energy/glu/commit/9925ae2dad5657c749f174e635df0c8209554a53))

- Add PR view command ([#51](https://github.com/BrightNight-Energy/glu/pull/51),
  [`368324e`](https://github.com/BrightNight-Energy/glu/commit/368324eb0fddc25688fc7f484d5fc9040c4dabae))

- Add view ticket command ([#50](https://github.com/BrightNight-Energy/glu/pull/50),
  [`d261da4`](https://github.com/BrightNight-Energy/glu/commit/d261da4b2f8e3863c9c43496bd341a184f5a29ec))

- Display mergeability status ([#53](https://github.com/BrightNight-Energy/glu/pull/53),
  [`ccf7a03`](https://github.com/BrightNight-Energy/glu/commit/ccf7a038464f3f78aa65c5e78be9099aabd8de3e))

- Optionally append PR number to merge commit title
  ([#52](https://github.com/BrightNight-Energy/glu/pull/52),
  [`a24cb92`](https://github.com/BrightNight-Energy/glu/commit/a24cb9231b0e76c4fa02fd0633a06e7c95ebd2b0))

- Support AI-generated PR titles and add update command
  ([#48](https://github.com/BrightNight-Energy/glu/pull/48),
  [`4ddcd2c`](https://github.com/BrightNight-Energy/glu/commit/4ddcd2c3c54e4e0c751dfe77768c85c9d0abc8bc))


## v2.4.0 (2025-07-18)

### Features

- Enhance PR merge workflow with PR diff context and panel refactoring
  ([`d979d0d`](https://github.com/BrightNight-Energy/glu/commit/d979d0d7c8fa8f00436e27a0e43fc96e47aa5f39))


## v2.3.4 (2025-07-17)

### Bug Fixes

- Fallback to built-in pr template when repo does not have own pr template
  ([`4cc09cc`](https://github.com/BrightNight-Energy/glu/commit/4cc09cc6725c17433aa638ae44c6b92af4b69e73))


## v2.3.3 (2025-06-25)

### Bug Fixes

- Make body optional on ticket create
  ([`874dff0`](https://github.com/BrightNight-Energy/glu/commit/874dff06f4eb35d89f8b4c30844fc00002403ec4))

- Make jira ticket optional on merge
  ([`e8dd070`](https://github.com/BrightNight-Energy/glu/commit/e8dd0705dec065598ecc000379faa8c67e462f89))

- Trim large diffs to respect model context limits
  ([`7669186`](https://github.com/BrightNight-Energy/glu/commit/7669186240c21fd2ba374b438a14f66553306e14))


## v2.3.2 (2025-06-16)

### Bug Fixes

- Respect repo.delete_branch_on_merge setting when merging prs
  ([`160c8f0`](https://github.com/BrightNight-Energy/glu/commit/160c8f0f758b58a8f288741cc519a91a71d9f2c8))

- Suppress 'not found' error when source branch auto-deleted
  ([`4935b1a`](https://github.com/BrightNight-Energy/glu/commit/4935b1ab304a66eb6fa8c9de41e185b5adbc5dba))


## v2.3.1 (2025-06-16)

### Bug Fixes

- Skip waiting ci checks in merge flow
  ([`e23898d`](https://github.com/BrightNight-Energy/glu/commit/e23898da4171ef336963c3930fdc97658005469d))


## v2.3.0 (2025-06-16)

### Features

- Add branch column to commit list
  ([`c8e9ad4`](https://github.com/BrightNight-Energy/glu/commit/c8e9ad4ac257f257aa1481e21727aeda815c0182))


## v2.2.0 (2025-06-16)

### Bug Fixes

- Modularize command structure and add error suppression
  ([`c043b6a`](https://github.com/BrightNight-Energy/glu/commit/c043b6afc7ba90d30e6effe3a64f7dbc43d5eaf2))

### Features

- Add 'generated with glu' tag to ai-created prs and tickets
  ([`7671106`](https://github.com/BrightNight-Energy/glu/commit/76711068374de0ea8cac98e3312558dec4ae8c29))

- Add commit list and commit count commands
  ([`addf91a`](https://github.com/BrightNight-Energy/glu/commit/addf91aaa4d5531e341afcb3ee623c08348d2b9d))


## v2.1.0 (2025-06-15)

### Features

- Add ai-driven final commit message generation and pr merge command
  ([`69118b5`](https://github.com/BrightNight-Energy/glu/commit/69118b5fdf8e0a0da35007dcc1c9b7761e05c787))


## v2.0.4 (2025-06-14)

### Bug Fixes

- Detect and inject jira ticket placeholder in pr descriptions
  ([`ad3843f`](https://github.com/BrightNight-Energy/glu/commit/ad3843f6142d3b3f785779238163fbe62ef8c635))


## v2.0.3 (2025-06-13)

### Bug Fixes

- Continue PR creation when ticket is skipped instead of returning early
  ([#33](https://github.com/BrightNight-Energy/glu/pull/33),
  [`7827f47`](https://github.com/BrightNight-Energy/glu/commit/7827f479ff9eafd75371b74154b8373e53f0e93f))

### Refactoring

- Add testing to commands ([#32](https://github.com/BrightNight-Energy/glu/pull/32),
  [`175503e`](https://github.com/BrightNight-Energy/glu/commit/175503e731aa8aa23856d7c393aa62623a59ca31))


## v2.0.2 (2025-06-06)

### Bug Fixes

- Fix glu --help without config ([#31](https://github.com/BrightNight-Energy/glu/pull/31),
  [`5d4d65f`](https://github.com/BrightNight-Energy/glu/commit/5d4d65f48aa5ce082557a3135f0bf8be8e4cc1eb))

- Support python 3.10+ ([#29](https://github.com/BrightNight-Energy/glu/pull/29),
  [`0b190e0`](https://github.com/BrightNight-Energy/glu/commit/0b190e0f2d13a86c3515c63036ddd2d62a5bb993))


## v2.0.1 (2025-06-02)

### Bug Fixes

- Remove glean chat provider support ([#27](https://github.com/BrightNight-Energy/glu/pull/27),
  [`256c5bb`](https://github.com/BrightNight-Energy/glu/commit/256c5bb0d5e5415da9e0e674b0af371a3f61e150))


## v2.0.0 (2025-06-02)

### Features

- Support multiple ai providers and model selection
  ([`00fe3e9`](https://github.com/BrightNight-Energy/glu/commit/00fe3e94abeb2edb7450b800034dc23efa74ee63))


## v1.6.0 (2025-06-01)

### Features

- Add README and build publish step to ci ([#25](https://github.com/BrightNight-Energy/glu/pull/25),
  [`986ff3b`](https://github.com/BrightNight-Energy/glu/commit/986ff3b5567990bb10c0e065c55a5d752e4bb82c))


## v1.5.0 (2025-06-01)

### Features

- Interactive config init, dry-run commits & config refactor
  ([#21](https://github.com/BrightNight-Energy/glu/pull/21),
  [`e504947`](https://github.com/BrightNight-Energy/glu/commit/e5049475d07e32879801e26d6b3f6214cca70cfb))


## v1.4.0 (2025-05-31)

### Features

- Support local git operations and ai-driven commit/ticket generation
  ([#20](https://github.com/BrightNight-Energy/glu/pull/20),
  [`a5a1066`](https://github.com/BrightNight-Energy/glu/commit/a5a106696e31d6f043c9e8c9ee4431f58899b23b))


## v1.3.1 (2025-05-31)

### Bug Fixes

- Add version command to `glu` ([#16](https://github.com/BrightNight-Energy/glu/pull/16),
  [`69e1334`](https://github.com/BrightNight-Energy/glu/commit/69e1334ca24b4920220481989c87f3c91d1ce49e))


## v1.3.0 (2025-05-31)

### Features

- Add ability to generate Jira tickets with AI
  ([#14](https://github.com/BrightNight-Energy/glu/pull/14),
  [`f2b3d75`](https://github.com/BrightNight-Energy/glu/commit/f2b3d758276aa5539d1ca19af53be4005884c722))


## v1.2.0 (2025-05-26)

### Features

- Cli improvements ([#12](https://github.com/BrightNight-Energy/glu/pull/12),
  [`8d4c922`](https://github.com/BrightNight-Energy/glu/commit/8d4c9223b37ce19d18c44fd50cfb8eab83c29fbc))


## v1.1.0 (2025-05-26)

### Features

- Add support for using OpenAI, rather than Glean
  ([#10](https://github.com/BrightNight-Energy/glu/pull/10),
  [`23958ae`](https://github.com/BrightNight-Energy/glu/commit/23958ae9a1484957a41e4aa1155c3ee2367026f8))


## v1.0.1 (2025-05-26)

### Bug Fixes

- Fix to semantic release in ci/cd ([#8](https://github.com/BrightNight-Energy/glu/pull/8),
  [`02f50d4`](https://github.com/BrightNight-Energy/glu/commit/02f50d4f0cdef5cb53f74f4cedce3c5a0a3a9ba2))


## v1.0.0 (2025-05-26)

- Initial Release

## v0.0.1 (2025-05-25)

### Features

* Initial commit
