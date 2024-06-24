
  

<h1>How to have your model verified in the eWaterCycle platform</h1>

  

<h3>Step 1: Create a public github repository with your model(if it doesn't exist yet)</h3>
The eWaterCycle testing framework can only verify models from public github repositories, thus you should create one that includes your model and a few other files mentioned in the forthcoming steps.


  

<h3>Step 2: Create a submission.yml file and put it in your public repo</h3>

  In the eWaterCycle testing repo you can see a few .yaml example submission files. They contain all the information about what to include and what format to use in your own submission file. Below you can see a screenshot of one of these example submission files, which is how a proper submission for the leaky-bucket hydrological model (https://github.com/eWaterCycle/leakybucket-bmi) would look like.![example-Submission.png](https://i.postimg.cc/W43Try66/example-Submission.png)



After creating the aforementioned submission file with the correct values for your model, upload the result to your public repository so that the eWaterCycle testing framework can read from it.
  

<h3>Step 3:  Create a pull request to have your model verified</h3>

  The pull request should start with "add model:", otherwise the testing framework will not recognize it as a valid verification request. The pull request should ONLY INCLUDE 1 CHANGE: a modification of the models.txt file, in which you add your model name and the link to its repository ON TOP OF THE TXT FILE. Feel free to modify other details in the pull request.
  

<h3>Step 4: Pass the automatic tests</h3>

After creating the pull request and if it fulfills the requirements mentioned above, automatic tests will be ran on your model. If they pass, there is a high likelihood that your model will be approved as a verified model in the eWaterCycle platform. If they fail, your model WILL NOT be approved. After each run, the test results can be downloaded from the link that is automatically commented under the submission pull request (unless you failed to fulfill the previous steps, in which case the tests won't even run on the model and will fail immediately).In order to prevent the tests failing, you can view the test results and improve upon their feedback or even import the eWaterCycle testing framework testing package and run the tests locally (there is a full guide on how to have your model tested locally within this package, feel free to go through it for directions).

