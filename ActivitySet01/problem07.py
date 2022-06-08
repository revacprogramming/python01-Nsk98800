text = "X-DSPAM-Confidence:    0.8475"

temp = text.find(" : ")
end = text[temp+1 :]
number=float(end)
print number