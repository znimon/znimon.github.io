---
title: "Multimodal AI Models"
date: "2025-07-21 00:00:00 -0600"
tags: [ML, Machine Learning]
image:
  path: https://res.cloudinary.com/de8dxxflb/image/upload/c_pad,w_1200,h_630/v1753113538/multi_modal_vqwwdt.png
  alt: ""
description: ""
categories: [Machine Learning]
author: Zak
---

## 💬 Overview

Traditionally, AI models have focused on a single modality. Language models like ChatGPT handle text, while others process images, audio, or video separately. For AI to become more natural and capable, it needs to integrate multiple types of input, much like humans do. A human assistant can listen, read, and see to make sense of context. This post gives a high‑level look at how multimodal AI systems work, key research milestones, and some real‑world applications.

#### 💡 Example Applications

**Creative Generation (Text ⇄ Image/Video/Audio)**  
- Prototype a video game using placeholder assets generated from descriptions.  
- Extract key frames from a video clip and turn them into a stylized comic strip.  

**Multimodal Assistants (Chat + Vision + Voice)**  
- Point your camera at a foreign‑language menu and ask, “What are popular lunch choices in Austria?”  
- Enhance AI tutoring capabilities by generating visual explanations of STEM concepts.  

**Cross‑Modal Search**  
- Show a product photo and say, “Same style but blue and under $100.”  
- Say some lyrics to find the corresponding song.  

---

### How Models Handle Different Types of Input

Multimodal models must convert every input (text, images, audio, or video) into numeric form, but each modality follows its own encoding path. Let’s walk through how each type is formatted.

#### 🤖 Encoding Each Modality

##### **Text**: *Tokenization → Embedding*  
- Words or characters are split into *tokens* and passed through an embedding layer that maps each token to a numeric vector (think of a learned dictionary of vectors).  
- These vectors capture semantic meaning; large language models manipulate them and eventually map the results back to natural‑language output.

##### **Audio**: *Waveform → Spectrogram → Embedding*  
- The 1‑D audio signal is converted to a *spectrogram* (a time‑frequency image of pitch and energy).  
- A neural encoder turns each time slice into an *audio embedding* that preserves tone, inflection, and timbre.  
- Text transcripts and audio embeddings complement one another: transcripts clarify speech masked by noise, while tone can resolve ambiguous text.

##### **Images**: *Patch / Region Encoding*  
- A common approach is to divide images into patches (e.g., a 16 × 16 grid) or segment them into regions such as foreground objects versus background.  
- For each patch, an encoder extracts edges, shapes, and colors, producing a *visual embedding*.  
- Collectively, these vectors summarize the scene (e.g., “dog, green grass, blue sky”).  

##### **Video**: *Frames + Time Modeling*  
- A video is a sequence of frames (often with an audio track). Key frames are sampled and passed through the image encoder.  
- Temporal models such as 3D CNNs or Transformers that [attend](https://en.wikipedia.org/wiki/Attention_Is_All_You_Need) over time capture motion and continuity across frames.  
- Audio from the clip is processed via the audio pipeline above. The result is a time‑aligned stream of visual and audio embeddings representing the entire clip.

#### 🧩 Putting It Together: Unifying Modalities
No matter the modality, the key idea is that the input information becomes a bunch of vectors (lists of numbers). These vectors encode the information from the input-whether that is the semantic content of a sentence, the objects in an image, the frequencies in audio, or the events in a video. Once we have these embeddings, a multimodal model needs to integrate them so it can reason about them together.

---

### 🥪 Techniques for Combining Information Across Modalities

#### Unified Sequence (Token Fusion)
- Non‑text inputs are turned into “pseudo‑tokens.” An image encoder, for instance, outputs a sequence of patch embeddings that are prepended into the text token stream of a decoder‑only Transformer.  
- Requires minimal architectural changes. GPT‑style models can ingest the longer sequence unchanged (e.g., GPT‑4‑V, LLaVA).  
- **Best for:** Captioning, simple image Q&A, rapid prototyping with an existing LLM.

#### Cross‑Modal Attention / Two‑Stream Fusion
- Separate encoders process text and vision (or audio); cross‑attention layers let each stream query the other, or a dedicated fusion block merges them.  
- Requires custom architecture and heavier compute when fusion occurs at multiple layers.  
- **Best for:** Tasks needing tight coupling, like visual dialog or referring‑expression grounding.

#### Dual Encoders with Late Fusion (Contrastive Alignment)
- Two independent encoders map each modality into a shared embedding space, trained with a contrastive loss so matching pairs land close together (e.g., CLIP).  
- Fast similarity search, ideal for scanning millions of image–text pairs.  
- **Best for:** Retrieval, ranking, recommendation.

#### 🧩 Putting It Together: Technique Mix
Modern systems often mix these techniques. For example, a CLIP dual encoder creates vision embeddings that are then fed to an LLM as unified tokens or via a cross‑attention adapter.

---

<article class="px-1">
  <h1 class="dynamic-title">Timeline</h1>
  <div class="content">
    <div id="archives" class="pl-xl-3">

      <time class="year lead d-block">2011</time>
      <ul class="list-unstyled">
        <li>
          <span class="date day">28</span>
          <span class="date month small text-muted ms-1">Jun</span>
          <a href="https://www.researchgate.net/publication/221345149_Multimodal_Deep_Learning">
            Multimodal Deep Learning
          </a>
        </li>
      </ul>

      <time class="year lead d-block">2012</time>
      <ul class="list-unstyled">
        <li>
          <span class="date day">03</span>
          <span class="date month small text-muted ms-1">Dec</span>
          <a href="https://papers.nips.cc/paper_files/paper/2012/file/af21d0c97db2e27e13572cbf59eb343d-Paper.pdf">
            Multimodal Learning with Deep Boltzmann Machines
          </a>
        </li>
      </ul>

      <time class="year lead d-block">2015</time>
      <ul class="list-unstyled">
        <li>
          <span class="date day">07</span>
          <span class="date month small text-muted ms-1">Jun</span>
          <a href="https://www.cv-foundation.org/openaccess/content_cvpr_2015/papers/Vinyals_Show_and_Tell_2015_CVPR_paper.pdf">
            Show and Tell: A Neural Image Caption Generator
          </a>
        </li>
        <li>
          <span class="date day">03</span>
          <span class="date month small text-muted ms-1">May</span>
          <a href="https://openaccess.thecvf.com/content_iccv_2015/papers/Antol_VQA_Visual_Question_ICCV_2015_paper.pdf">
            VQA: Visual Question Answering
          </a>
        </li>
      </ul>

      <time class="year lead d-block">2016</time>
      <ul class="list-unstyled">
        <li>
          <span class="date day">17</span>
          <span class="date month small text-muted ms-1">May</span>
          <a href="https://arxiv.org/abs/1605.05396">
            Generative Adversarial Text to Image Synthesis
          </a>
        </li>
      </ul>

      <time class="year lead d-block">2019</time>
      <ul class="list-unstyled">
        <li>
          <span class="date day">06</span>
          <span class="date month small text-muted ms-1">Aug</span>
          <a href="https://arxiv.org/abs/1908.02265">
            ViLBERT
          </a>
        </li>
      </ul>

      <time class="year lead d-block">2021</time>
      <ul class="list-unstyled">
        <li>
          <span class="date day">24</span>
          <span class="date month small text-muted ms-1">Feb</span>
          <a href="https://arxiv.org/abs/2102.12092">
            Zero‑Shot Text‑to‑Image Generation
          </a>
        </li>
        <li>
          <span class="date day">26</span>
          <span class="date month small text-muted ms-1">Feb</span>
          <a href="https://arxiv.org/abs/2103.00020">
            Learning Transferable Visual Models From Natural Language Supervision
          </a>
        </li>
        <li>
          <span class="date day">20</span>
          <span class="date month small text-muted ms-1">Dec</span>
          <a href="https://arxiv.org/abs/2112.10752">
            High‑Resolution Image Synthesis with Latent Diffusion Models
          </a>
        </li>
      </ul>

      <time class="year lead d-block">2022</time>
      <ul class="list-unstyled">
        <li>
          <span class="date day">13</span>
          <span class="date month small text-muted ms-1">Apr</span>
          <a href="https://arxiv.org/abs/2204.06125">
            Hierarchical Text‑Conditional Image Generation with CLIP Latents
          </a>
        </li>
        <li>
          <span class="date day">29</span>
          <span class="date month small text-muted ms-1">Apr</span>
          <a href="https://arxiv.org/abs/2204.14198">
            Flamingo: A Visual Language Model for Few‑Shot Learning
          </a>
        </li>
        <li>
          <span class="date day">23</span>
          <span class="date month small text-muted ms-1">May</span>
          <a href="https://arxiv.org/abs/2205.11487">
            Photorealistic Text‑to‑Image Diffusion Models with Deep Language Understanding
          </a>
        </li>
      </ul>

      <time class="year lead d-block">2023</time>
      <ul class="list-unstyled">
        <li>
          <span class="date day">26</span>
          <span class="date month small text-muted ms-1">Jan</span>
          <a href="https://arxiv.org/abs/2301.11325">
            MusicLM: Generating Music From Text
          </a>
        </li>
        <li>
          <span class="date day">27</span>
          <span class="date month small text-muted ms-1">Feb</span>
          <a href="https://arxiv.org/abs/2302.14045">
            Language Is Not All You Need: Aligning Perception with Language Models
          </a>
        </li>
        <li>
          <span class="date day">06</span>
          <span class="date month small text-muted ms-1">Mar</span>
          <a href="https://arxiv.org/abs/2303.03378">
            PaLM‑E: An Embodied Multimodal Language Model
          </a>
        </li>
        <li>
          <span class="date day">15</span>
          <span class="date month small text-muted ms-1">Mar</span>
          <a href="https://arxiv.org/abs/2303.08774">
            GPT‑4 Technical Report
          </a>
        </li>
        <li>
          <span class="date day">17</span>
          <span class="date month small text-muted ms-1">Apr</span>
          <a href="https://arxiv.org/abs/2304.08485">
            Visual Instruction Tuning (LLaVA)
          </a>
        </li>
        <li>
          <span class="date day">09</span>
          <span class="date month small text-muted ms-1">May</span>
          <a href="https://arxiv.org/abs/2305.05665">
            ImageBind: One Embedding Space to Bind Them All
          </a>
        </li>
        <li>
          <span class="date day">11</span>
          <span class="date month small text-muted ms-1">Sep</span>
          <a href="https://arxiv.org/abs/2309.05519">
            NExT‑GPT: Any‑to‑Any Multimodal LLM
          </a>
        </li>
      </ul>

      <time class="year lead d-block">2024</time>
      <ul class="list-unstyled">
        <li>
          <span class="date day">15</span>
          <span class="date month small text-muted ms-1">Feb</span>
          <a href="https://blog.google/technology/ai/google-gemini-next-generation-model-february-2024/">
            Gemini 1.5 (Pro): 1 M‑token multimodal context
          </a>
        </li>
      </ul>

      <time class="year lead d-block">2025</time>
      <ul class="list-unstyled">
        <li>
          <span class="date day">05</span>
          <span class="date month small text-muted ms-1">Apr</span>
          <a href="https://ai.meta.com/blog/llama-4-multimodal-intelligence/">
            Llama 4‑V: Open‑weight natively multimodal model
          </a>
        </li>
        <li>
          <span class="date day">13</span>
          <span class="date month small text-muted ms-1">May</span>
          <a href="https://openai.com/index/hello-gpt-4o/">
            GPT‑4o: Real‑time text‑vision‑audio reasoning
          </a>
        </li>
      </ul>

    </div>
  </div>
</article>

## 📦 Closing Thoughts

What used to be a “cool, but sandboxed” multimodal demo is fast becoming an everyday utility. As models learn to weave together text, images, audio, and video, they become:

- **More natural**: Interacting the way humans do, across sight, sound, and language.  
- **More capable**: Creating new media and grounding language in the physical world.  
- **More demanding**: Requiring careful data curation, alignment, and increased compute.  

Though this is only a very broad overview, I hope it helps convey the core concepts behind multimodal models and their growing significance.

---

☕ [Buy me a coffee](https://www.buymeacoffee.com/znimon)
