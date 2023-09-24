#linearsearchproduct that takes the list of products and target product name as input

def linearSearchProduct(productList,targetPrduct):
  indices = []

  for index,product in enumerate(productList):
    if product == targetPrduct:
      indices.append(index)

  return indices

products = ["gown","saree","lehenga","saree","kurti","saree","western dress","saree"]
target1 = "saree"
target2 = "watch"
result1 = linearSearchProduct(products,target1)
result2 = linearSearchProduct(products,target2)
print(result1)
print(result2)