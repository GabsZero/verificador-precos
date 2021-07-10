from selenium import webdriver
import time

class CrawlerService:
    # this will hold information found in pages
    products = []

    def getResult(self):
        products = self.products
        self.products = []
        return products

    def searchInCasasBahia(self, search):
        driver = webdriver.Chrome()
        driver.get(f"https://www.casasbahia.com.br/{search}/b")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        time.sleep(5)  
        results = driver.find_elements_by_xpath("//*[@id='__next']/div[2]/div/div/div[4]/div[2]/div/article/ul")
        if(len(results) < 1):
            results = driver.find_elements_by_xpath("/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/article/ul")

        # loop over results
        for result in results:
            products = result.find_elements_by_tag_name("a")
            for product in products:
                try:
                    productInfo = {
                        'link': product.get_attribute('href'),
                        'imagem': product.find_element_by_tag_name('img').get_attribute('src'),
                        'nome': product.find_element_by_tag_name('p').text,
                        'preco': product.find_element_by_css_selector("div[class^='ProductPrice']").text
                    }
                except:
                    print('não foi possível adicionar o produto na lista')

                self.products.append(productInfo)
        
        driver.quit()