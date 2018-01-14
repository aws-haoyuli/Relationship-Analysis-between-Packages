def test_delete_user(app):
    app.session.login(username="admin", password="qa2017")
    app.users.delete()
    app.session.logout()

    # ПРОВЕРКА
    #wait.until(EC.presence_of_all_elements_located((By.XPATH, "//ul[@class='sb-list ng-scope']")))
    #self.assertNotIn("Auto.test.user", driver.find_element_by_xpath("//ul[@class='sb-list ng-scope']").text)

