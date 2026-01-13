^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package sync_tooling_msgs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

0.2.6 (2026-01-13)
------------------
* chore: more readme tuning
* chore: adhere to SYNC.TOOLING branding in readme
* chore: add license headers everywhere
* chore: update readme
* chore: use SPDX identifier in package.xml
* chore: more style fixes
* chore: fix import spacing
* chore: fix docstring spacing
* docs: add module docstring
* Contributors: Max SCHMELLER

0.2.5 (2025-08-27)
------------------
* chore: bump version to 0.2.5
* fix: allow negative delays in SlaveClockState as they occur in reality
* Contributors: Max SCHMELLER

0.2.4 (2025-08-05)
------------------
* chore: bump version to 0.2.4
* Contributors: Max SCHMELLER

0.2.3 (2025-07-07 19:09)
------------------------
* chore: bump versio to 0.2.3
* Contributors: Max SCHMELLER

0.2.2 (2025-07-07 17:02)
------------------------
* chore: bump version to 0.2.2
* Contributors: Max SCHMELLER

0.2.1 (2025-07-03)
------------------
* chore: bump version to 0.2.1
* Contributors: Max SCHMELLER

0.2.0 (2025-07-02)
------------------
* chore: version bump to 0.2.0
* feat: allow comments in diag tree
* chore: rephrase self reported clock states
* fix: remove superfluous `.status` from `flatten`ed trees
* chore: print Clock IDs nicely in string interpolation
* test: add clock ID print/parse test
* chore: include examples in tests
* chore: add usage examples
* chore: replace name+ip by frame_id for sensor clock IDs
* feat: add self reported clock state graph update type
* docs: document all protos
* docs: doc comments for utility functions
* docs: doc comments for some messages
* chore: remove unused import
* chore: add master_offset_ns field to ClockMasterUpdate
* fix(port_state): make all states either ok or error
* test: add tests for port/servo state diags
* chore(clock_id): raise if no ID is set
* chore: make GraphUpdate hashable
* chore: refactor tests to use fixtures
* chore: satisfy ruff
* chore(diag_tree): remove dead code
* feat(clock_id): make ClockIds parsable from strings
* chore: replace frame_id by sensor_id
* fix(diag_tree): allow to_diag_tree(DiagTree)
* build: fix CMake script after adding new protos
* chore: change from diagnostic in PHC2SYS update to raw state values
* chore: add option to print PortId without domain
* chore: make PortState diagnosable
* chore: move diag_tree helpers to sync_tooling_msgs
* chore: fix ruff and type checker complaints
* add function to make clock types readable
* fix: handle empty clock IDs correctly
* feat: make ClockId, PortId hashable
* chore: delete accidentally added pyc files
* chore: create LICENSE
* chore(cmake): update to reflect namespace changes, add new proto files to list
* WIP
* chore: fix phc2sys_update, rename clock_status_update to be more expressive, add clock_alias_update
* fix: export correct includes and targets
* chore: add time difference measurement proto
* feat: add graph update protos [WIP]
* chore: generate python type information too
* chore: make project buildable with both `uv` and `colcon`
* chore: initial protos and build system for Python/C++ mostly done
* Contributors: Max SCHMELLER, Max Schmeller
