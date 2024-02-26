FROM budtmo/docker-android:latest
USER root

# add permission 777(read + write + execute) to directory
RUN chmod -R 777 /home/androidusr/

# Install Python
RUN apt-get update && apt-get install -y python3 python3-pip

# Copy the APK file
COPY hutbot_apk/signed.apk  /app/signed.apk

#Copy files
COPY requirements.txt .
RUN pip3 install --no-cache-dir wheel --user
RUN pip3 install --no-cache-dir -r requirements.txt --user
USER 1001

# Expose necessary ports
EXPOSE 6080 4723 5554 5555

# Set environment variables
ENV DEVICE="Samsung Galaxy S6" \
    APPIUM=true \
    CONNECT_TO_GRID=true \
    APPIUM_HOST="127.0.0.1" \
    APPIUM_PORT=4723 \
    SELENIUM_HOST="172.17.0.1" \
    SELENIUM_PORT=4444 \
    MOBILE_WEB_TEST=true
