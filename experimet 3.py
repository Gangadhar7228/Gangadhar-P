integer_value=int(input ("enter an integer:"))
float_value=float(input("enter a floating point number:"))
text_value=input("enter a string:")
bool_text=input("enter boolean value (true/false):").strip().lower()
boolean_value=(bool_text=="true")

print("\n---values and data types---")
print(integer_value,type(integer_value))
print(float_value,type(float_value))
print(text_value,type(text_value))
print(boolean_value,type(boolean_value))

print("\n---arithmetic operations---")
print("sum=",integer_value+float_value)
print("product=",integer_value+float_value)

print("\n---string operations---")
print("concatenation=",text_value+"python")
print("repetition=",text_value*2)
print("length=",len(text_value))

print("\n---boolean operation---")
print("length=",len(text_value))