# By: Lana Jehad Gazawi - 3230601010

print("="*50)
print(" "*10 + "⚡ ELECTRICITY BILLING SYSTEM ⚡")
print("="*50)
print("Please enter customer details to calculate bill...")
print("="*50)


customer_count = 1

def calculate_electricity_bill():
    global customer_count
    try:
        
        customer_id = input("\nEnter Customer ID: ")
        if not customer_id.isdigit():
            raise ValueError("Customer ID must contain digits only.")
            
        customer_fname = input("Enter Customer First Name: ").strip()
        if not customer_fname.replace(" ", "").isalpha():
            raise ValueError("Customer name must contain letters only.")
            
        customer_lname = input("Enter Customer Last Name: ").strip()
        if not customer_lname.replace(" ", "").isalpha():
            raise ValueError("Customer name must contain letters only.")
            
        units_input = input("Enter Units Consumed: ")
        if not units_input.strip():
           raise ValueError("Units consumed cannot be empty.")
        units = float(units_input)
        if units < 0:
           raise ValueError("Units consumed cannot be negative.")
    
       
        bill_amount = 0.0
        if units <= 50:
            bill_amount = units * 0.50
        elif units <= 150:
            bill_amount = (50 * 0.50) + ((units - 50) * 0.75)
        elif units <= 250:
            bill_amount = (50 * 0.50) + (100 * 0.75) + ((units - 150) * 1.20)
        else:
            bill_amount = (50 * 0.50) + (100 * 0.75) + (100 * 1.20) + ((units - 250) * 1.50)
          
        surcharge = bill_amount * 0.20
        total_bill = bill_amount + surcharge
        
        
        print("\n" + "="*50)
        print(f"SUMMARY FOR CUSTOMER #{customer_count}")
        print("="*50)
        print(f"Customer ID: {customer_id}")
        print(f"Customer Name: {customer_fname} {customer_lname}")
        print(f"Units Consumed: {units} kWh")
        print(f"Total Bill: {total_bill:.2f} JD")
        print("="*50)

        with open("electricity_bills.txt", "a") as file:
       
            if customer_count == 1:
                file.write("\n" + "="*30 + "\n")
                file.write("OFFICIAL CUSTOMERS LIST\n")
                file.write("="*30 + "\n")

            record = (f"Customer {customer_count}\n"
                      f"{'-'*30}\n"
                      f"ID: {customer_id}\n"
                      f"Name: {customer_fname} {customer_lname}\n"
                      f"Units: {units} kWh\n"
                      f"Total: {total_bill:.2f} JD\n"
                      f"{'-'*30}\n")
            file.write(record)

        print(f"Customer {customer_count} was saved successfully!")
        
      
        customer_count += 1 
      
    except ValueError as e:
        print("\nError:", e)

while True:
    calculate_electricity_bill()
    
    cont = input("\nDo you want to add another customer? (yes/no): ").strip().lower()
    if cont != 'yes':
        print("\n" + "="*50)
        print(" "*10 + "Existing System... Goodbye!")
        print("="*50)
        break