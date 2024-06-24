
  

<h1>How to incorporate the testing framework package into eWaterCycle</h1>

The testing framework package does properly test each incoming model, but was designed and tested to work for pull requests to it's own package, not as an additional installment that detects pull requests in other packages. However, incorporating it into the main eWaterCycle package should not be difficult, as it should only require a few changes to the workflows. 

Namely, all the steps of the workflow "Model verification" that are related to extracting the source branch's files (all the test files) and running the appropriate .py files (tests) locally should be replaced with importing the testing package and running its corresponding files for each of the "running" steps remotely with all the dependencies(or creating ur own .py testing files that call the same methods from the imported package as the test-running files do locally). The other workflow should work perfectly fine without any issue when incorporated.

It is also worth to note that the workflow requires a self-hosted machine to run on. Though I am fairly certain such a machine has already been set up, if not, it can be set up in the main eWaterCycle package using [this guide](https://docs.github.com/en/enterprise-cloud@latest/actions/hosting-your-own-runners/managing-self-hosted-runners/adding-self-hosted-runners). All the required packages for the self-hosted machine can be found in the requirements.txt file.




  
