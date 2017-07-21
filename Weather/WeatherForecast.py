import subprocess

condition = subprocess.check_output("pywu forecast condition", shell=True)
condition = condition.replace("\n", "")

low = subprocess.check_output("pywu forecast low_c", shell=True)
low = low.replace("\n", "")
low = low + "C"

high = subprocess.check_output("pywu forecast high_c", shell=True)
high = high.replace("\n", "")
high = high + "C"

print "Forecast today is %s, with highs of %s and lows of %s" % (condition,high,low)
