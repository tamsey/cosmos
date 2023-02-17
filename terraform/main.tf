provider "azurerm"  {
    features ()
}


resource "azurermresource_group" "new_resourcegrp" {
location = "eastus"
name = "terraform"
}