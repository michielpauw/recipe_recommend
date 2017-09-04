from bs4 import BeautifulSoup
import urllib.request

recipe_link = urllib.request.urlopen(
    "https://www.ah.nl/allerhande/recept/R-R1188623/thaise-noedels-met-varkensreepjes-en-wortellinten")
recipe_html = recipe_link.read()
recipe_link.close()

soup = BeautifulSoup(recipe_html, "html.parser")  # take html and make searchable tree
# print(soup.title.string)  # get page title
# print(soup.body)

# 4 personen, 615 kcal voedingswaarden, 25 min. bereiden
#
# <h2 class="hidden-phones">Naast échte noedels eet je vanavond oranje noedel-lookalikes: wortellinten. </h2>
# </header> </section>
# section class="info hidden-phones">
# <ul class="short">
# <li><div class="icon icon-course"></div><span>hoofdgerecht</span></li>
# <li><div class="icon icon-people"></div><span><a class="servings js-scaler__scrollto">4 personen</a></span></li>
# <li><div class="icon icon-nutritional"></div><span>615 kcal <a class="more" href="#">voedingswaarden</a></span></li>
# <li class="cooking-time">
# <ul>
# <li content="PT25M"><div class="icon icon-time"></div>25 min. bereiden</li>
# </ul> </li> </ul> <form action="/allerhande/cartridges/PageSlot/PageSlot.jsp;WLSESSIONID=J8NM_d6lwMqBJyeutBGT4VYxG0rMne29Y4CEVC1CwrEFnsTXBIER!2085701064?_DARGS=/allerhande/cartridges/RecipeDetail2.0/Summary.jsp.rateRecipeForm" id="rateRecipeForm" method="POST" style="display: none;"><div style="display:none"><input name="_dyncharset" type="hidden" value="UTF-8"/> </div><div style="display:none"><input name="_dynSessConf" type="hidden" value="-1184681002497417532"/> </div><input name="/allerhande/rating/RateRecipeFormHandler.recipeId" type="hidden" value="1188623"/><input name="_D:/allerhande/rating/RateRecipeFormHandler.recipeId" type="hidden" value=" "/><input id="submitRatingValue" name="/allerhande/rating/RateRecipeFormHandler.rating" size="1" type="hidden" value="3"/><input name="_D:/allerhande/rating/RateRecipeFormHandler.rating" type="hidden" value=" "/><input name="/allerhande/rating/RateRecipeFormHandler.rateRecipe" type="hidden" value="true"/><input name="_D:/allerhande/rating/RateRecipeFormHandler.rateRecipe" type="hidden" value=" "/><div style="display:none"><input name="_DARGS" type="hidden" value="/allerhande/cartridges/RecipeDetail2.0/Summary.jsp.rateRecipeForm"/> </div></form>
# <div class="rating ">

sect = soup.find_all('h2')
for i in range(len(sect)):
    print('*'*20)
    print(i)
    print(sect[i])

# Ingrediënten

# <section class="js-ingredients ingredients">
# <h4>Ingrediënten</h4>
# <div class="js-scaler scaler" data-max-servings-number="40" data-min-servings-number="1" data-scale-number="4" data-serving-type="personen" data-serving-type-plural="personen" data-serving-type-singular="persoon" data-servings-number="4" data-servings-scale-number="1" id="scaler-wrapper">
# <div class="scaler__scale">
# <span class="js-scale-servings scaler__label">4 personen</span>
# <div class="scaler__buttons">
# <a class="js-scale scaler__button scaler__button--down " data-scale-action="down"></a>
# <a class="js-scale scaler__button scaler__button--up " data-scale-action="up"></a>
# </div>
# </div>
# </div>
# <div class="recipe-disclaimer--left">
# <div class="recipe-disclaimer js-scaler-disclaimer">
# <div class="recipe-disclaimer__close js-scaler-disclaimer__close"></div>
# <div class="recipe-disclaimer__content">
# <p><strong>Let op!</strong> Je wijkt af van het aantal personen waarvoor dit recept ontwikkeld is. Bereiding, video, kook- en oventijden en keukenspullen kunnen hierdoor ook afwijken. <a data-dax="faq.clickout" href="https://www.ah.nl/klantenservice/29676/Allerhande/31317/Recepten" target="_blank">Lees de tips</a></p>
# </div>
# </div>
# </div>
# <ul class="list shopping ingredient-selector-list">
# <li itemprop="ingredients">
# <a class="js-ingredient ingredient-selector js-ingredient-is-selected" data-additional-info="" data-default-label="500 g winterpenen" data-description-plural="winterpenen" data-description-singular="winterpeen" data-quantity="500" data-quantity-unit-plural="g" data-quantity-unit-singular="g" data-search-term="winterpeen" href="#" rel="nofollow" title="Verwijder dit ingrediënt uit selectie">
# <span class="js-label label">500 g winterpenen</span><span class="icon icon-check"></span> </a> </li>
# <li itemprop="ingredients">
# <a class="js-ingredient ingredient-selector js-ingredient-is-selected" data-additional-info="" data-default-label="1 bosje salade-ui" data-description-plural="salade-uien" data-description-singular="salade-ui" data-quantity="1" data-quantity-unit-plural="bosjes" data-quantity-unit-singular="bosje" data-search-term="salade-ui" href="#" rel="nofollow" title="Verwijder dit ingrediënt uit selectie">
# <span class="js-label label">1 bosje salade-ui</span><span class="icon icon-check"></span> </a> </li>
# <li itemprop="ingredients">
# <a class="js-ingredient ingredient-selector js-ingredient-is-selected" data-additional-info="" data-default-label="2 eieren" data-description-plural="eieren" data-description-singular="ei" data-quantity="2" data-quantity-unit-plural="" data-quantity-unit-singular="" data-search-term="ei" href="#" rel="nofollow" title="Verwijder dit ingrediënt uit selectie">
# <span class="js-label label">2 eieren</span><span class="icon icon-check"></span> </a> </li>
# <li itemprop="ingredients">
# <a class="js-ingredient ingredient-selector js-ingredient-is-selected" data-additional-info="" data-default-label="400 g bloemkoolrijst" data-description-plural="" data-description-singular="bloemkoolrijst" data-quantity="400" data-quantity-unit-plural="g" data-quantity-unit-singular="g" data-search-term="bloemkoolrijst" href="#" rel="nofollow" title="Verwijder dit ingrediënt uit selectie">
# <span class="js-label label">400 g bloemkoolrijst</span><span class="icon icon-check"></span> </a> </li>
# <li itemprop="ingredients">
# <a class="js-ingredient ingredient-selector js-ingredient-is-selected" data-additional-info="" data-default-label="2 el arachideolie" data-description-plural="" data-description-singular="arachideolie" data-quantity="2" data-quantity-unit-plural="el" data-quantity-unit-singular="el" data-search-term="arachideolie" href="#" rel="nofollow" title="Verwijder dit ingrediënt uit selectie">
# <span class="js-label label">2 el arachideolie</span><span class="icon icon-check"></span> </a> </li>
# <li itemprop="ingredients">
# <a class="js-ingredient ingredient-selector js-ingredient-is-selected" data-additional-info="" data-default-label="225 g Thaise rijstnoedels" data-description-plural="" data-description-singular="Thaise rijstnoedels" data-quantity="225" data-quantity-unit-plural="g" data-quantity-unit-singular="g" data-search-term="Thaise rijstnoedels" href="#" rel="nofollow" title="Verwijder dit ingrediënt uit selectie">
# <span class="js-label label">225 g Thaise rijstnoedels</span><span class="icon icon-check"></span> </a> </li>
# <li itemprop="ingredients">
# <a class="js-ingredient ingredient-selector js-ingredient-is-selected" data-additional-info="" data-default-label="400 g magere varkensreepjes" data-description-plural="" data-description-singular="magere varkensreepjes" data-quantity="400" data-quantity-unit-plural="g" data-quantity-unit-singular="g" data-search-term="magere varkensreepjes" href="#" rel="nofollow" title="Verwijder dit ingrediënt uit selectie">
# <span class="js-label label">400 g magere varkensreepjes</span><span class="icon icon-check"></span> </a> </li>
# <li itemprop="ingredients">
# <a class="js-ingredient ingredient-selector js-ingredient-is-selected" data-additional-info="" data-default-label="80 ml soja-gemberdressing" data-description-plural="" data-description-singular="soja-gemberdressing" data-quantity="80" data-quantity-unit-plural="ml" data-quantity-unit-singular="ml" data-search-term="soja-gemberdressing" href="#" rel="nofollow" title="Verwijder dit ingrediënt uit selectie">
# <span class="js-label label">80 ml soja-gemberdressing</span><span class="icon icon-check"></span> </a> </li>
# </ul>
# <div id="ingredients_to_shoplist">
# <a class="js-ingredients-to-shoplist-button" data-thumbnail="https://static.ah.nl/static/recepten/img_089735_220x162_JPG.jpg" href="#" onclick="sendAddIngredientsEventToKrux()">
# <div aria-hidden="true" class="icon icon-plus"></div>
# <span>Zet deze ingrediënten op mijn lijst</span>
# </a>-

# tags

# </ul> </section>
# <section class="tags">
# <h6>Tags</h6>
# <ul class="tags">
# <li><a href="/allerhande/recepten-zoeken/__/N-26z3?tag=aziatisch">aziatisch</a></li>
# <li><a href="/allerhande/recepten-zoeken/__/N-26zl?tag=thais">thais</a></li>
# <li><a href="/allerhande/recepten-zoeken/__/N-26x1?tag=wat eten we vandaag">wat eten we vandaag</a></li>
# <li><a href="/allerhande/recepten-zoeken/__/N-26wz?tag=roerbakken/wokken">roerbakken/wokken</a></li>
# </ul> </section>
# <section class="source">
# <h6>Ook te zien in</h6>
