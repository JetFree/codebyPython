city = 'города - масква, лондон, париж, берлин...'
corrected_city = city.replace("масква", "москва").replace("-", "—")[:-2]
title_city = corrected_city.title()
print(title_city)
