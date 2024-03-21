# Automation Frame Work


### Development environment

- Pycharm: https://www.jetbrains.com/pycharm/.
- Appium Server GUI/CLI
- Android Studio/AVD stand alone:
- compatible version: Appium v2.0.0
- compatible version: uiautomator2@3.0.3


- To install required library.
```zsh
pip3 install --no-cache-dir -r requirements.txt --user
```


## Start emulator (with all data is cleared)
```bash
emulator @Android34 -wipe-data
```

## Start emulator on deadless mode
```bash
emulator -no-window -no-audio @Android34
```

## Start appium server
```bash
appium -p 0.0.0.0:4723
```

## download the latest apk file and store it in
```bash
./apks/
```



## inspect current apk
```bash
adb shell
dumpsys window displays | grep -E ‘mCurrentFocus’
io.pizzahut.hutbot.qa/io.yum.MainActivity
```


## Run a testscript
```bash
pytest testcases/test_login.py --alluredir=./allure_report
#to see output, will get both pass and fail shown in results
-rA
#to see more details in result(v = verbose)
-v
#keyword matching test will run
-k routine
#use regular expression
-k "routine or login"
-k "not routine"
#use with marker
-m smoke
-k "smoke or regression"
```

## run allure-report

## Run a testscript
```bash
allure serve ./allure_report
```

## BUILD DOCKER IMAGE
```bash
docker build -t appium_android  . 
```


## RUN DOCKER CONTAINER
```bash
sudo docker run --privileged -d -p 6080:6080 -p 4723:4723 -p 5554:5554 -p 5555:5555 -e DEVICE="Samsung Galaxy S10"   --name <docker_container_name> <image_name> 
```

## add permission 777(read + write + execute) to directory
```bash
# add permission 777(read + write + execute) to directory
RUN chmod -R 777 /home/androidusr/
```

## build a image
```bash
docker build -t appium_android  .
```

## run docker container
```bash
docker run --privileged --user root -d -p 6080:6080 -p 4723:4723 -p 5554:5554 -p 5555:5555 -e DEVICE="Samsung Galaxy S6"   --name automation_pom_container appium_android

```

## find app_package
```bash
adb shell dumpsys window | grep -E 'mCurrentFocus'
```

## Download and setup JAVA_HOME automatically
```bash
1 - Check is Java is installed 
2 - Download brew: /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
3 - Install JAVA with brew: brew install openjdk@11
4 - Verify installation: java -version
5 - Set Java Home 
```

## Activate venv
```bash
python3 -m venv env                    
source env/bin/activate                                                       
pip3 install -r requirements.txt
```

## Modifying .bash_profile or .zprofile (to set *_HOME manually)
```bash
cd ~/
open .zprofile
open .bash_profile 
nano ~/.zshrc


```

## Run config for selenium grid
```bash
#create event-bus:
java -jar selenium-server-4.18.1.jar event-bus --publish-events tcp://192.168.1.6:4442 --subscribe-events tcp://192.168.1.6:4443 --port 5557

#create sessionqueue:
java -jar selenium-server-4.18.1.jar sessionqueue --port 5559

#create sessions:
java -jar selenium-server-4.18.1.jar sessions --publish-events tcp://192.168.1.6:4442 --subscribe-events tcp://192.168.1.6:4443 --port 5556

#create distributor:
java -jar selenium-server-4.18.1.jar distributor --publish-events tcp://192.168.1.6:4442 --subscribe-events tcp://192.168.1.6:4443 --sessions http://192.168.1.6:5556 --sessionqueue http://192.168.1.6:5559 --port 5553 --bind-bus false

#create router:
java -jar selenium-server-4.18.1.jar router --sessions http://192.168.1.6:5556 --distributor http://192.168.1.6:5553 --sessionqueue http://192.168.1.6:5559 --port 4444

#create node
java -jar selenium-server-4.18.1.jar node --publish-events tcp://192.168.1.6:4442 --subscribe-events tcp://192.168.1.6:4443
```


## Run config for selenium grid using config file
```bash
cd /Users/lephat/PycharmProjects/automation_mobile_pom/selenium_grid
appium --config appium1.yml
appium --config appium2.yml
java -jar selenium-server-4.18.1.jar node --config node_emulator.toml
java -jar selenium-server-4.18.1.jar node --config node_realdevice.toml
java -jar selenium-server-4.18.1.jar hub
```

## Run on Browser Stack
```bash
browserstack-sdk pytest -s testcases/test_routines.py
```
