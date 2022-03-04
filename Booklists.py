booklists=[]

count=int(input("Enter number of books"))
for i in range(0,count):
  d=  {
    "book_name":input("Enter name of book"),
    "author_name":input("Enter author_name"),
    "price":int(input("Enter prices")),
    "publisher_name":input("Enter publisher name")

    }
  booklists.append(d)
# print(booklists)
for i in booklists:
  print(i)
# _________________________________________________________________________
student_data=[
  {
    "name":"Ramya",
    "marks": [
      {
        "english":34,
        "science":85
      }
    ]
  },
      {
"name":"divya",
"marks": [
      {
        "english":34,
        "science":85
      }

    ]
      }
  ]
for i in student_data:
  print(i["name"])
  for j in i["marks"]:
    print(j["english"])
