from threading import Thread
import webcontroller.webcontroller as wcs
import website.webcontroller_client as wcc

t_wcs = Thread(target = wcs.start, daemon = True)
t_wcc = Thread(target = wcc.start)
t_wcs.start()
t_wcc.start()
t_wcc.join()