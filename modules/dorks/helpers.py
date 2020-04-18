
#!/usr/bin/env python

from __future__ import (absolute_import, division, print_function)

from common.colors import run, W, end, good, bad, que, info, bannerblue

class DorkManual():

    def __init__(self,select=None):
        self.select = select

    def dorkslist(self):
        print("""
        −−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−
        %sWordPress          Joomla               Prestashop
        −−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−%s
        blaze              comjce               columnadverts          
        catpro             comfabrik            soopabanners           
        cherry             comjdownloads        vtslide                
        dm                 comfoxcontact        simpleslideshow        
        fromcraft                               productpageadverts     
        synoptic                                productpageadvertsb    
        shop                                    jro_homepageadvertise  
        revslider                               attributewizardpro     
        adsmanager                              oneattributewizardpro  
        inboundiomarketing                      attributewizardpro_old 
        wysija                                  attributewizardpro_x   
        powerzoomer                             advancedslider         
        showbiz                                 cartabandonmentpro     
        jobmanager                              cartabandonmentpro_old 
        injection                               videostab              
        thumbslider                             wg24themeadministration
                                                fieldvmegamenu         
                                                wdoptionpanel          
                                                pk_flexmenu            
                                                pk_vertflexmenu        
                                                nvn_export_orders      
                                                tdpsthemeoptionpanel   
                                                masseditproduct
    """ % (W, end))

    def wp_dorkTable(self):
        print("""
        WordPress          
        ---------          
        blaze              
        catpro             
        cherry             
        dm                 
        fromcraft          
        synoptic           
        shop               
        revslider          
        adsmanager         
        inboundiomarketing 
        wysija             
        powerzoomer        
        showbiz            
        jobmanager         
        injection          
        thumbslider        
                """)

    def joo_dorkTable(self):
        print("""
        Joomla       
        ------       
        comjce       
        comfabrik    
        comjdownloads
        comfoxcontact
                 """)

    def ps_dorkTable(self):

        print("""
        Prestashop
        -----------
        columnadverts          
        soopabanners           
        vtslide                
        simpleslideshow        
        productpageadverts     
        productpageadvertsb    
        jro_homepageadvertise  
        attributewizardpro     
        oneattributewizardpro  
        attributewizardpro_old 
        attributewizardpro_x   
        advancedslider         
        cartabandonmentpro     
        cartabandonmentpro_old 
        videostab              
        wg24themeadministration
        fieldvmegamenu         
        wdoptionpanel          
        pk_flexmenu            
        pk_vertflexmenu        
        nvn_export_orders      
        tdpsthemeoptionpanel   
        masseditproduct
                """)

    def loko_dorkTable(self):
        print("""
        Lokomedia       
        ------              
                """)

    def dru_dorkTable(self):
        print("""
        Drupal       
        ------              
                """)

    def list(self):
        if self.select == 'all':
            self.dorkslist()

        if self.select == 'wordpress':
            self.wp_dorkTable()
        
        if self.select == 'joomla':
            self.joo_dorkTable()
        
        if self.select == 'prestashop':
            self.ps_dorkTable()
        
        if self.select == 'Lokomedia':
            self.loko_dorkTable()
        
        if self.select == 'Drupal':
            self.dru_dorkTable()
