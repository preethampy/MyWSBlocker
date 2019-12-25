# PyWSBlocker
This is a simple project that blocks the website's from a list we provide between the time we choose.So this simple blocker can be usefull if you have a guest to your machine or for children who uses your machine to access some websites that you dont want them to visit or is more specific if you are running a small company and you want to limit access to some sites that your clients waste their time on in some specific periods.This is a simple 1kb yet a powerfull project.I have created this keeping begginer like you in mind,so i have added detailed documentation for each and every step so that its easy for you.you are welcome to clone,make changes,suggestions and finding bugs.
## Before you import/Download/clone
* Running the siteblocker.py file directly will give you an error because the code we have written works with OS file called 'hosts' file.To block and unblock any website, first we need to make changes in this file and that changes will be done programmatically by our python script.So run the command prompt as administrator and execute siteblocker.py file.
* If you want this file/script to continuosly block the websites as per the program we have written & without intteruption (like after restart,after power up,after shut down)follow the below steps
1. On windows OS,Search for task scheduler in search box.
2. Click on create task and give it a name.
3. Check "Run with highest privileges"
4. Click on trigger > new > at dropdown select "At start up" > ok
5. Click on action > new > Browse to the project directory and select the siteblocker.pyw > ok
6. Click on conditions > uncheck "power" section and ok or apply
7. Restart the computer and you are done 
## Troubleshooting
* If the websites in the list are not getting blocked,then please run the script through command prompt as administrator again
or if you already did that,then wait for sometime in the brower till it reads the hosts file or just restart your browser just once and it should work normal.
