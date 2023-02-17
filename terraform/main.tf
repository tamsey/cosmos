provider "azurerm" {
    features {}
}
variable "location" {
  default = "eastus"
}
variable "name" {
  default = "new-resource1"
}
resource "azurerm_resource_group" "new-resource1" {
  location = var.location
  name = var.name
  tags = {
    Name = "Training"
    Day = "6"
  }
}
resource "azurerm_cosmosdb_account" "GlobalDocumentDB" {
  name                      = var.name
  location                  = var.location
  resource_group_name       = azurerm_resource_group.new-resource1.name
  offer_type                = "Standard"
  kind                      = "GlobalDocumentDB"
  enable_automatic_failover = false
  geo_location {
    location          = var.location
    failover_priority = 0
  }
  consistency_policy {
    consistency_level       = "BoundedStaleness"
    max_interval_in_seconds = 300
    max_staleness_prefix    = 100000
  }
}
