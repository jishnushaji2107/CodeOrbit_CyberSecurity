def check_password(password):
    score=0
    suggestions=[]
    if len(password)>=8:
        score+=1
    else:
        suggestions.append("Use atleast 8 characters.")
    if any(c.isupper() for c in password):
        score+=1
    else:
        suggestions.append("Add an uppercase letter")
    if any(c.islower() for c in password):
        score+=1
    else:
        suggestions.append("Add a lowercase letter")
    if any(c.isdigit()for c in password):
        score+=1
    else:
        suggestions.append("Add a number")
    if any(c.isalnum()for c in password):
        score+=1
    else:
        suggestion.append("Add a special character")
    if score==5:
        print("Password strength:Strong")
    elif score>=3:
        print("Password strength:Moderate")
    else:
        print("Password strength:Weak")

    if suggestions:
        print("\Suggestions to improve")
        for suggestion in suggestions:
            print("-",suggestion)

password=input("Enter a password to check:")
check_password(password)
