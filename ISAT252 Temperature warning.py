## Practice with if/elif/else if. I'll use this code for my thermocouple sensor
temperature = int(input())
if temperature > 25.00
    GPIO.output(GPIO_LED, GPIO.HIGH)
    print("WARNING. TOO HOT")
elif tempertature < 15.00:
    GPIO.output(GPIO_LED, GPIO.HIGH)
    print("WARNING. TOO COLD")
else:
    GPIO.output(GPIO_LED, GPIO.LOW)
    

