# Automation Frame Work


### Development environment

- Pycharm: https://www.jetbrains.com/pycharm/.
- Appium Server GUI/CLI
- Android Studio/AVD stand alone:


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

## Run a testscript
```bash
pytest TestCases/test_login.py --alluredir=./allure_report
```

## run allure-report

```python
allure serve ./allure-report
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


## Modifying .bash_profile or .zprofile (to set JAVA_HOME manually)
```bash
cd ~/
open .zprofile
open .bash_profile 
nano ~/.zshrc


```


