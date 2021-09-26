# infra

Kubernetes related infrastructure and manifests for the application and it's basic configuration.
Currently only tested on Minikube.

Excluding `app`, this needs to be moved to another repository.
A helm chart should be created for the application manifests.

`nginx.conf.template` is used in docker - the nginx conf in the configmap is slightly difference as since nginx and the api are in the same pod in k8s `localhost` can be used, but the name of the container must be used with docker-compose.

## Infrastructure Diagram

![Diagram](diagram.png)

## CI/CD Pipeline Diagram (desired)

![CID Diagram](backend-ci-pipeline-revision-1.png)

Diagram feedback:
* Remove the "Run Unit Tests"
* How do i know what version of postgres to run, e.g matching it in production? Is it static?
* Figure out how to comment on the issue if there is an issue, or pull request etc...
    * If it is a PR, `GITHUB_REF` will contain 
* Maybe only run destroy on branch - it could check for a .destroy file ( which could contain the workspace name) and have manual actions to prevent accidental deletion.

Destroy flow:
1. Create .destroy file
2. Enter the following json into the file
```
{
    "destroyInfo": {
        "branchName": "CURRENT_BRANCH_CHANGEME",
        "destroy": True
    }
}
```
3. Commit file
4. Push file