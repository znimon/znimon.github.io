---
title: "Hello World"
date: "2025-04-17 00:00:00 -0600"
categories: [Template]
tags: [Hello World]
description: Short summary of the post. # Not needed will truncate blog content if omitted
image:
  path: /assets/img/posts/2025-04-17-hello-world/image.png # Blog post hero image resolution of 1200 x 630.
  alt: Blog Hero Image
pin: true # pin one or more posts to the top of the home page
math: true
---


# Hello World

## Overview

1. Create new md file in _posts
2. Add images to assets/img/posts/<post_name>


## Links

For new posts refer to the documentation [here](https://chirpy.cotes.page/posts/write-a-new-post/)

## Images
![Desktop View](/assets/img/posts/2025-04-17-hello-world/inline.png){: width="700" height="400" }

## Video

{% include youtube.html id='LPZh9BOjkQs' %}

## Math
<!-- Block math, keep all blank lines -->

$$
LaTeX_math_expression
$$

<!-- Equation numbering, keep all blank lines  -->

$$
\begin{equation}
  LaTeX_math_expression
  \label{eq:label_name}
\end{equation}
$$

Can be referenced as \eqref{eq:label_name}.

<!-- Inline math in lines, NO blank lines -->

"Lorem ipsum dolor sit amet, $$ LaTeX_math_expression $$ consectetur adipiscing elit."

<!-- Inline math in lists, escape the first `$` -->

1. \$$ LaTeX_math_expression $$
2. \$$ LaTeX_math_expression $$
3. \$$ LaTeX_math_expression $$

