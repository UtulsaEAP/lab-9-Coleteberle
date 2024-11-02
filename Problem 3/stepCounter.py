def feet_to_steps(user_feet):
   #write your code here
   steps = user_feet/2.5
   return steps

if __name__ == '__main__':
    #take input feet steps here
    #store it into the function
    user_feet = float(input())
    #print your steps here
    feet_to_steps(5280)