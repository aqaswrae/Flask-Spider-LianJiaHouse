import requests
from lxml import etree

# url = 'http://qd.lianjia.com/ershoufang/pg2'
# headers = {
# 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
# }
#
# content = requests.get(url,headers).text
# # print(content)
# tree = etree.HTML(content)
#
# # tag = '//ul[@class="sellListContent"]/li[1]//div[@class="tag"]/span/text()'
#
# # t = tree.xpath(tag)
# # print(t)
#
# path = '//ul[@class="sellListContent"]/li[1]'
# def get_tag(path, tree):
#     tag = '//div[@class="tag"]/span/text()'
#     substances = tree.xpath(path + tag)
#     strr = ''
#     if substances:
#         for i in substances:
#             strr += i+' '
#     # print(substances[0])
#     print(strr)
#     return strr
# get_tag(path,tree)










# <!DOCTYPE html>
# <html>
#   <head>
#     <title>房产数据</title>
#   </head>
#   <body>
#     <h1>房产数据</h1>
#     <table>
#       <thead>
#         <tr>
#           <th>选择</th>
#           <th>地址</th>
#           <th>面积</th>
#           <th>价格</th>
#           <th>操作</th>
#         </tr>
#       </thead>
#       <tbody>
#         {% for property in properties %}
#         <tr>
#           <td><input type="checkbox" name="property_ids" value="{{ property.id }}"></td>
#           <td>{{ property.address }}</td>
#           <td>{{ property.area }}</td>
#           <td>{{ property.price }}</td>
#           <td><button type="button" onclick="deleteProperty({{ property.id }})">删除</button></td>
#         </tr>
#         {% endfor %}
#       </tbody>
#     </table>
#     <button type="submit" onclick="deleteSelected()">删除所选</button>
#   </body>
#   <script>
#     function deleteProperty(propertyId) {
#       if (confirm('确定要删除该房产数据吗？')) {
#         // 发送 AJAX 请求以删除房产数据
#         fetch(`/delete/${propertyId}`, { method: 'DELETE' })
#           .then(response => window.location.reload())
#           .catch(error => console.error(error));
#       }
#     }
#
#     function deleteSelected() {
#       let selectedProperties = Array
#         .from(document.querySelectorAll('input[name="property_ids"]:checked'))
#         .map(input => Number(input.value));
#       if (selectedProperties.length > 0 && confirm('确定要删除所选房产数据吗？')) {
#         // 发送 AJAX 请求以删除所选的房产数据
#         fetch('/delete', {
#             method: 'POST',
#             headers: { 'Content-Type': 'application/json' },
#             body: JSON.stringify({ propertyIds: selectedProperties })
#           })
#           .then(response => window.location.reload())
#           .catch(error => console.error(error));
#       }
#     }
#   </script>
# </html>