'''
მომხმარებელს შეეკითხეთ მისი ასაკი, ასევე შეეკითხეთ რამდენი წლით სურს დროში მოგზაურობა და დაპრინტეთ
რამდენი წლის იქნება დროში მოგზაურობის შემდეგ
'''


current_age = int(input("whats your age?:"))
years_to_travel = int(input("რანსები ხნით გსურს დროში მოგზაურობა"))

new_age = current_age + years_to_travel
print("After traveling back", years_to_travel, "years, you would be", new_age, "years old.")
