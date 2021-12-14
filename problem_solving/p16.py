# Epidemiology
# https://dmoj.ca/problem/ccc20j2
# When a person has a disease, they infect exactly  other people but only on the very next day. 
# No person is infected more than once. We want to determine when a total of more than  people 
# have had the disease.


P = int(input("How many people is too many sick people:\n"))
N = int(input("How many people are sick on the first day:\n"))
R = int(input("How many people did each person infect on the first day:\n"))

def main():
  infected = N
  cases = infected
  day = 0

  while True:
    print(f"day={day}\tinfected={infected}\tcases={cases}")

    if cases >= P:
        break

    infected *= R
    cases += infected
    day += 1

  print(f"\nReached {P} cases on day {day}")

main()





