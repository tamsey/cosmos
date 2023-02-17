provider "azurerm" {
    features {}
}
resource "azurerm_resource_group" "newresource" {
  location = "eastus"
  name = "tamanna"
  tags = {
    Name = "Day"
    Day = "5"
  }
}


