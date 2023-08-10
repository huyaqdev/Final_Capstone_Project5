[![CircleCI](https://dl.circleci.com/status-badge/img/gh/huyaqdev/Final_Capstone_Project5/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/huyaqdev/Final_Capstone_Project5/tree/main)

# CloudDevopsCapstone Project5
AWS Cloud Devops Engineer program

In this Capstone project, the project could be devide into steps by steps:
- Setup AWS configure
- Use CircleCI to implement CICD for application
- Build Application pipeline
- Build k8s cluster
- Build Docker image and upload to Docker Hub repository
- Deploy Docker container to Kubernetes cluster
- Build Ansible roles, CloudFormation stacks to create network, nodegroup as well as deploy eks cluster

The pipeline follow CircleCI my_workflow:
- build:
	+ This job used to prepare the working environment for project and check lint syntax,...
- docker_upload:
	+ This job used to build the docker image with tag, then push/upload the image to Docker Hub repository
- deployment_infra:
	+ This job used to create the cloudformation stack to build and prepare everything like: EKS network, EKS cluster, EKS Nodegroup and host management,...
- configure_infra:
	+ This job used to authentication AWS, set up AWS congfigure options as well as config Kubernetes cluster
- cluster_configure:
	+ This job used to setup service and prepare deployment, it also get and store Elastic Load Balancer DNS to local file
- docker_deployment:
	+ This last job used to deploy docker image (from Docker Hub repository) to Kubernetes cluster

Screenshots results:
- CircleCI pipeline workflow successfully:

- CloudFormation stacks:
+ Image: cloud_formations_stacks.PNG
- Lint successfully
+ Image: lint_success.PNG
- Lint fail
+ Image: lint_failed.PNG
- EC2 instances
+ Image: elc2_instances.PNG
- Run EKS failure
+ Image: EKS-fail.PNG
- EKS successfully
+ Image: eks.PNG
- Run Pipeline successfully
+ Image: circle_ci_pipe_success.PNG
- Docker image application deployment
+ URL: https://hub.docker.com/repository/docker/huyaqdev/clouddevops/general
- GitHub code of project
+ URL: https://github.com/huyaqdev/Final_Capstone_Project5
- Web application result:
+ URL: http://a6806861dc95943419ecb5ca3caec07c-1766187062.us-east-1.elb.amazonaws.com


