# Marketplace and Database Project

## Overview
This project serves as the backend for managing marketplaces and the associated product data. It provides RESTful API endpoints for accessing and managing product data, reviews, and other related information. This project is designed to work in conjunction with (the https://github.com/alex827a/Django_and_recomendation_distilbert_system.git) which handles recommendations and additional automation processes.

## Features
- **RESTful API**: Provides endpoints to access and manage product data.
- **Admin Interface**: Manage products, categories, reviews, and marketplaces through the Django admin interface.
- **Data Storage**: Stores product and review data in a relational database.

## Project Structure
- **Models**:
  - `Product`: Represents a product in the marketplace.
  - `Review`: Represents a review for a product.
  - `Marketplace`: Represents a marketplace where products are sold.
  - `Category`: Represents a category of products.

- **API Endpoints** (requires token authentication):
  - `GET /api/products/`: Retrieve a list of products.
  - `GET /api/products/<id>/`: Retrieve details of a specific product.
  - `GET /api/reviews/`: Retrieve a list of reviews.
  - `GET /api/reviews/<id>/`: Retrieve details of a specific review.
  - `GET /api/marketplaces/`: Retrieve a list of marketplaces.
  - `GET /api/marketplaces/<id>/`: Retrieve details of a specific marketplace.

## Prerequisites
- Python 3.10+
- Django 5.0.3+
- Necessary Python packages as listed in `requirements.txt`

