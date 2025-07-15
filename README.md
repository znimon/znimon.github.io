# Blog

- Deploy locally:  
`bundle exec jekyll serve`
- Cloudinary image resizer:
```
# For a hero-sized image (1200×630)
python transform_cloudinary_url.py \
  https://res.cloudinary.com/your_cloud_name/image/upload/v1234567890/sample.jpg \
  --size hero

# For an inline image (700×400)
python transform_cloudinary_url.py \
  https://res.cloudinary.com/your_cloud_name/image/upload/v1234567890/sample.jpg \
  --size inline
  ```