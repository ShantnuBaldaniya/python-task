a={
  "Shoes": [100, 200, 150],
  "Bags": [50, 300],
  "bottle":[20,20,20,50]
} 

new={}

for product,sales in a.items():
    new[product]=sum(sales)
    
print(new)