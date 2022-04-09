# Integration Testing Lightctl

In order to test Lightctl, an API refresh credential is needed towards a working
Lightup cluster. The API credential can be stored in a specific place or in the
default location.

The test creates and deletes objects but partial runs of the test will result in
objects being leftover that may need manual cleanup.

**NOTE** This test should not be run frequently but only as integration test to validate
with actual Lightup cluster and real Email accounts.

**Do not run lightctl integration test against production clusters.**
