# AI Engineer Roadmap - Python to Agentic AI

Daily execution plan evolved from the original 90-day AI/ML roadmap into a mentor-reviewed 100-day AI Engineer path. The repository name remains `90-Days-AI-ML-Roadmap` for now, but the roadmap direction is now Python to Agentic AI.

This roadmap preserves completed Days 1-14 and updates Day 15 onward toward job-ready AI engineering: classical ML, deployment, PyTorch, computer vision, NLP, transformers, LLM apps, fine-tuning, serving, agents, and a final capstone.

## How to Use This Roadmap

- Each day is a unit of work, around 3-4 focused hours.
- Some advanced days may take longer, especially QLoRA, serving, MCP, and multi-agent systems.
- Depth is more important than speed.
- If I cannot explain the topic clearly, I should not mark the day complete.
- Every major phase should end with documentation, project review, and interview notes.
- The strongest 4-6 projects should become flagship portfolio projects; the rest can remain learning labs.

## Execution Rules

- Concepts before coding.
- Metrics before model comparison.
- Evaluate every model.
- Document every portfolio project.
- Prefer fewer polished flagship projects over many shallow projects.
- Weekly review is mandatory.
- Advanced topics like QLoRA, MCP, and multi-agent systems are stretch goals unless earlier foundations are strong.
- Do not skip evaluation, documentation, or interview explanation where relevant.

## Phase Map

| Phase | Days | Focus |
| --- | --- | --- |
| Phase 1 | Days 1-14 | Foundations |
| Phase 2 | Days 15-24 | Core Machine Learning |
| Phase 3 | Days 25-30 | Unsupervised ML + Deployment |
| Phase 4 | Days 31-40 | Deep Learning with PyTorch |
| Phase 5 | Days 41-51 | Computer Vision |
| Phase 6 | Days 52-61 | Natural Language Processing |
| Phase 7 | Days 62-74 | Transformers & Generative AI / LLMs |
| Phase 8 | Days 75-80 | Fine-tuning, Quantization & Serving |
| Phase 9 | Days 81-91 | Agents & Agentic AI |
| Phase 10 | Days 92-100 | Capstone, Portfolio & Interviews |

---

## Phase 1: Foundations (Days 1-14)

Completed day folders include `guide.md` learning notes where available, along with the daily README, resources, project code, and screenshots.

### Day 01 ✅

Topics:

* Python refresher
* NumPy basics
* Arrays
* Vectorization

Project/Task:

* Student Marks Analyzer

Deliverable:

* NumPy practice
* GitHub setup

---

### Day 02 ✅

Topics:

* 2D NumPy Arrays
* Pandas Introduction
* DataFrames
* Basic Data Exploration

Project/Task:

* Student Performance Analyzer

Deliverable:

* DataFrame creation
* Statistics analysis

---

### Day 03 ✅

Topics:

* Missing Values
* Data Cleaning
* Data Types
* Filtering Data
* Duplicate Detection
* Value Counts
* GroupBy
* Sorting

Project/Task:

* Employee Data Analyzer

Deliverable:

* Detect missing values
* Fill missing values
* Filter employees by salary
* Analyze departments using value counts and grouped summaries

---

### Day 04 ✅

Topics:

* Data Visualization
* Matplotlib Basics

Project/Task:

* Employee Salary Dashboard

Deliverable:

* Bar charts
* Histograms
* Pie charts
* Saved PNG chart outputs

---

### Day 05 ✅

Topics:

* Seaborn Basics
* Correlation Visualization

Project/Task:

* Employee Insights Dashboard

Deliverable:

* Barplots
* Heatmaps
* Distribution plots
* Boxplots
* Scatterplots
* Saved PNG chart outputs

---

### Day 06 ✅

Topics:

* Exploratory Data Analysis (EDA)

Project/Task:

* Employee Data Analysis Report

Deliverable:

* EDA report
* Dataset overview
* Missing value and duplicate checks
* EDA visualizations
* Final insights and conclusions

---

### Day 07 ✅

Topics:

* Revision
* Interview Questions

Project/Task:

* Weekly Review

Deliverable:

* Week 1 summary
* Revision checklist
* Interview questions

---

### Day 08 ✅

Topics:

* Feature Engineering Basics
* Encoding

Project/Task:

* Dataset Preparation

Deliverable:

* Create engineered features
* Encode categorical columns
* Save prepared dataset

---

### Day 09 ✅

Topics:

* Feature Scaling
* Normalization
* Standardization

Project/Task:

* Data Preprocessing Pipeline

Deliverable:

* Apply min-max normalization
* Apply standardization
* Save preprocessed dataset

---

### Day 10 ✅

Topics:

* Train/Test Split

Project/Task:

* Dataset Splitting Tool

Deliverable:

* Split data into train and test sets
* Explain features and target
* Save train and test datasets

---

### Day 11 ✅

Topics:

* Introduction to Machine Learning

Project/Task:

* ML Workflow Notes

Deliverable:

* Explain features and target
* Summarize the ML workflow
* Compare regression and classification

---

### Day 12 ✅

Topics:

* Linear Regression Theory

Project/Task:

* House Price Prediction (Part 1)

Deliverable:

* Explain linear regression theory
* Identify features and target
* Visualize Area vs Price relationship

---

### Day 13 ✅

Topics:

* Linear Regression Implementation

Project/Task:

* House Price Prediction (Part 2)

Deliverable:

* Implement simple linear regression
* Calculate MAE, MSE, RMSE, and R2 Score
* Save prediction chart

---

### Day 14 ✅

Topics:

* Foundation audit
* Skills checklist
* Completed project review
* Weak area identification
* ML core preparation

Project/Task:

* Foundation Audit and ML Core Preparation

Deliverable:

* Review Days 1-13
* Create a skills checklist
* Identify weak projects and weak topics
* Prepare the folder plan for Phase 2

Practical outcome:

* A clear transition document that shows what is done, what needs improvement, and how the next phase becomes more job-focused.

Why this day matters:

* A serious checkpoint prevents the roadmap from becoming only daily output without career direction.

---

## Phase 2: Core Machine Learning (Days 15-24)

Learn the ML workflow and core algorithm families quickly: concepts first, metrics once, then models in evolution order.

### Day 15

Topics:

* Statistics for ML
* ML workflow
* Supervised vs unsupervised learning

Project/Task:

* Statistics + ML Workflow Reference

Deliverable:

* Small Pandas/NumPy statistics examples
* One-page ML workflow document
* Regression vs classification comparison

Practical outcome:

* A reusable foundation reference for the rest of the roadmap.

Why this day matters:

* Statistics and workflow thinking make later models easier to evaluate and explain.

---

### Day 16

Topics:

* SQL SELECT, WHERE, ORDER BY, GROUP BY
* Aggregations
* Joins

Project/Task:

* SQL Business Queries Practice

Deliverable:

* Business-style dataset
* Basic and join queries
* Documented results and business meaning

Practical outcome:

* Start building data access skills expected in ML, data science, and AI engineering roles.

Why this day matters:

* Most real AI/ML work begins with retrieving and understanding data.

---

### Day 17

Topics:

* Real dataset EDA and cleaning
* Missing values and duplicates
* Business questions

Project/Task:

* EDA + SQL Business Analytics (Portfolio Project 1)

Deliverable:

* Join tables and answer business questions
* EDA report with insights

Practical outcome:

* A portfolio project that connects SQL, EDA, and business analysis.

Why this day matters:

* Recruiters can understand this project even without deep ML context.

---

### Day 18

Topics:

* Features and target
* Train/validation/test split
* Data leakage and baselines

Project/Task:

* Supervised ML Project Setup (Portfolio Project 2)

Deliverable:

* Select dataset and define target/features
* Create splits
* Document leakage risks
* Set a baseline

Practical outcome:

* A supervised ML project starts with a clean, honest setup.

Why this day matters:

* Data leakage can make beginner projects look better than they really are.

---

### Day 19

Topics:

* Improved linear regression
* Logistic regression
* Prediction probabilities

Project/Task:

* Regression & Classification Baselines

Deliverable:

* Train both baselines
* Generate predictions and probabilities
* Save models with `joblib`

Practical outcome:

* Baseline models for regression and classification.

Why this day matters:

* Strong baselines give later model comparisons real meaning.

---

### Day 20

Topics:

* Classification metrics
* Regression metrics
* Choosing the right metric

Project/Task:

* Model Evaluation Report + Metrics Reference

Deliverable:

* Compute and explain each metric
* Plot a confusion matrix
* Build one metrics cheatsheet reused across the roadmap

Practical outcome:

* A reference that supports model comparison in every future phase.

Why this day matters:

* Metrics guide model decisions; they should be understood before comparing models.

---

### Day 21

Topics:

* KNN
* Naive Bayes
* SVM and kernels

Project/Task:

* Baseline Model Comparison

Deliverable:

* Train KNN, Naive Bayes, and SVM
* Compare against logistic regression in one table
* Note which model fits which case

Practical outcome:

* A practical comparison of distance-based, probabilistic, and margin-based models.

Why this day matters:

* Knowing why model families differ is more useful than memorizing names.

---

### Day 22

Topics:

* Decision Trees
* Random Forest
* Boosting with XGBoost, LightGBM, or CatBoost
* Feature importance and SHAP

Project/Task:

* Tree-Based & Boosting Comparison

Deliverable:

* Train tree, Random Forest, and boosting models
* Compare with previous baselines
* Explain feature importance with SHAP where appropriate

Practical outcome:

* A stronger tabular ML comparison with interpretable results.

Why this day matters:

* Tree-based models are common in practical supervised ML projects.

---

### Day 23

Topics:

* scikit-learn Pipeline
* ColumnTransformer
* Cross-validation
* Overfitting and underfitting
* Hyperparameter tuning

Project/Task:

* ML Pipeline + Tuning

Deliverable:

* Numeric and categorical preprocessing pipeline
* Cross-validation results
* Tuned model with saved best parameters

Practical outcome:

* A cleaner, more reliable ML workflow.

Why this day matters:

* Pipelines and cross-validation prevent many common beginner mistakes.

---

### Day 24

Topics:

* Interpretation and error analysis
* Limitations
* README and requirements
* Resume bullets and interview Q&A

Project/Task:

* Supervised ML Finalization + Core ML Interview Pack

Deliverable:

* Finalize Portfolio Project 2
* Results, screenshots, setup instructions, and limitations
* Resume bullets and interview answers

Practical outcome:

* A GitHub-ready supervised ML project.

Why this day matters:

* A project is portfolio-ready only when it can be explained, reproduced, and reviewed.

---

## Phase 3: Unsupervised ML + Deployment (Days 25-30)

### Day 25

Topics:

* K-Means, hierarchical clustering, DBSCAN
* Choosing k with elbow and silhouette
* PCA

Project/Task:

* Customer Segmentation (Portfolio Project 3)

Deliverable:

* Scale features
* Train clusters and choose k
* Profile segments
* PCA visualization

Practical outcome:

* A clear unsupervised learning project with business-style segment explanations.

Why this day matters:

* Clustering is useful when there is no target label but patterns still matter.

---

### Day 26

Topics:

* Imbalanced data
* Resampling and class weights
* Threshold tuning
* Precision-recall trade-off

Project/Task:

* Imbalanced Classification Mini-Project

Deliverable:

* Analyze class distribution
* Train baseline and balanced models
* Tune threshold
* Document trade-offs

Practical outcome:

* A focused project showing why accuracy can be misleading.

Why this day matters:

* Many real classification problems are imbalanced.

---

### Day 27

Topics:

* Streamlit basics
* App inputs and outputs
* Input validation

Project/Task:

* Streamlit ML App

Deliverable:

* UI for a saved model
* Accept inputs and display predictions
* Save screenshots

Practical outcome:

* A simple interactive demo for a portfolio ML project.

Why this day matters:

* A UI makes your work easier for non-technical reviewers to try.

---

### Day 28

Topics:

* FastAPI basics
* `/predict` endpoint
* Pydantic schema
* Validation and error handling

Project/Task:

* FastAPI Prediction API

Deliverable:

* `/predict` endpoint loading a saved model
* Input validation and API docs
* Tested sample JSON requests

Practical outcome:

* A beginner model-serving API.

Why this day matters:

* AI engineers often need to expose models through APIs.

---

### Day 29

Topics:

* Project structure
* Requirements or `pyproject`
* Docker basics
* Reproducibility
* Basic testing

Project/Task:

* Deployment-Ready Project + Tests

Deliverable:

* Organized model, app, source, and requirements
* Basic Dockerfile
* Simple preprocessing and prediction tests
* Setup/run documentation

Practical outcome:

* A deployable project structure rather than a loose script.

Why this day matters:

* Reproducibility and testing are part of engineering quality.

---

### Day 30

Topics:

* Portfolio audit
* Project storytelling
* Interview Q&A

Project/Task:

* ML Engineering Review & Interview Pack

Deliverable:

* Review Projects 1-3
* Fix gaps
* Resume bullets
* Answers on clustering, PCA, imbalance, APIs, deployment, and testing

Practical outcome:

* A documented checkpoint before deep learning.

Why this day matters:

* Each phase should end with proof of understanding, not only code output.

---

## Phase 4: Deep Learning with PyTorch (Days 31-40)

Raw PyTorch first: write training loops by hand before higher-level wrappers.

### Day 31

Topics:

* Tensors and operations
* CPU/GPU basics
* Autograd

Project/Task:

* PyTorch Tensor & Autograd Practice

Deliverable:

* Compare tensors with NumPy
* Compute gradients with autograd
* Notes on raw PyTorch basics

Practical outcome:

* A hands-on PyTorch foundation.

Why this day matters:

* Tensors and autograd are the base of modern deep learning code.

---

### Day 32

Topics:

* Neurons, layers, and forward pass
* ReLU, GELU, sigmoid, softmax
* Why non-linearity matters

Project/Task:

* Neural Network Concepts + Forward Pass

Deliverable:

* Explain neurons, layers, and activations
* Small forward-pass example
* Interview questions

Practical outcome:

* A simple bridge from math intuition to PyTorch models.

Why this day matters:

* Neural networks are easier to debug when the forward pass is clear.

---

### Day 33

Topics:

* MSE and cross-entropy loss
* Backpropagation
* SGD, Momentum, RMSProp, Adam, AdamW

Project/Task:

* Backprop & Optimizer Notes

Deliverable:

* Do the chain rule by hand once
* Explain parameter updates
* Compare optimizers

Practical outcome:

* Clear training mechanics notes for interviews and debugging.

Why this day matters:

* Optimizers and gradients explain how models actually learn.

---

### Day 34

Topics:

* Dataset and DataLoader
* Batching
* Custom training loop
* Checkpoints

Project/Task:

* First PyTorch Training Loop from Scratch

Deliverable:

* Full training loop by hand
* Track loss
* Save a checkpoint

Practical outcome:

* A reusable PyTorch training template.

Why this day matters:

* Training loops transfer to CV, NLP, and generative AI work.

---

### Day 35

Topics:

* Fully connected network
* Training and evaluation
* Accuracy

Project/Task:

* MNIST MLP Classifier

Deliverable:

* Load MNIST
* Train an MLP
* Evaluate test accuracy

Practical outcome:

* First complete deep learning classifier.

Why this day matters:

* MNIST gives a simple full workflow before harder image tasks.

---

### Day 36

Topics:

* Overfitting
* Dropout
* BatchNorm or LayerNorm
* Weight decay and early stopping
* Learning rate schedules

Project/Task:

* MNIST Improvement Experiment

Deliverable:

* Plot train/validation curves
* Apply dropout or BatchNorm
* Document what changed and why

Practical outcome:

* Evidence-based model improvement.

Why this day matters:

* Deep learning needs training diagnosis, not only final accuracy.

---

### Day 37

Topics:

* Convolution, kernels, stride, padding, pooling
* Why CNNs beat MLPs on images

Project/Task:

* CNN Image Classifier (Part 1)

Deliverable:

* Build a simple CNN
* Train on Fashion-MNIST or CIFAR
* Explain each layer

Practical outcome:

* Start an image classifier with CNN fundamentals.

Why this day matters:

* CNNs are still essential for practical computer vision understanding.

---

### Day 38

Topics:

* CNN evaluation
* Confusion matrix
* Misclassification review

Project/Task:

* CNN Image Classifier (Part 2)

Deliverable:

* Evaluate CNN
* Review misclassified images
* Save predictions and charts

Practical outcome:

* A stronger CNN report with error analysis.

Why this day matters:

* Error review reveals what accuracy hides.

---

### Day 39

Topics:

* Experiment tracking with Weights & Biases or MLflow
* GPU training
* Reproducibility
* Mixed precision and gradient accumulation

Project/Task:

* Tracked Training Run

Deliverable:

* Log one run
* Compare 2-3 configurations
* Train on GPU where available

Practical outcome:

* Basic experiment discipline.

Why this day matters:

* Experiment tracking becomes important as models and runs multiply.

---

### Day 40

Topics:

* Deep learning documentation
* Limitations
* Interview prep

Project/Task:

* Deep Learning Finalization (Portfolio Project 4) + Interview Pack

Deliverable:

* README with dataset, model, metrics, limitations, and predictions
* Interview answers on autograd, backprop, CNNs, overfitting, Adam vs SGD, and BatchNorm
* Resume bullets

Practical outcome:

* A polished deep learning learning-lab project.

Why this day matters:

* Deep learning projects need evidence, explanation, and limitations.

---

## Phase 5: Computer Vision (Days 41-51)

Work up the CV task hierarchy: classification, detection, and segmentation.

### Day 41

Topics:

* Images as tensors and channels
* Augmentation
* Transfer learning idea
* CV task hierarchy

Project/Task:

* CV Concepts Notebook

Deliverable:

* Augmentation examples
* One-page map of CV tasks and metrics

Practical outcome:

* A mental map of classification, detection, and segmentation.

Why this day matters:

* CV tasks require different labels, models, and metrics.

---

### Day 42

Topics:

* Binary, multi-class, and multi-label image classification
* Scratch CNN vs transfer learning

Project/Task:

* Image Classifier - Scratch + Transfer (Portfolio Project 5)

Deliverable:

* Train a scratch CNN
* Transfer-learn a pretrained backbone such as ResNet or EfficientNet
* Compare the two

Practical outcome:

* A stronger image classification project.

Why this day matters:

* Transfer learning is a practical baseline for many CV projects.

---

### Day 43

Topics:

* LeNet to AlexNet, VGG, Inception, ResNet, DenseNet, EfficientNet, ViT, ConvNeXt
* What problem each architecture solved

Project/Task:

* Architecture Evolution Notes + Backbone Swap

Deliverable:

* Timeline explaining why each model exists
* Swap backbones and compare accuracy/speed

Practical outcome:

* A practical understanding of CV architecture evolution.

Why this day matters:

* Knowing the evolution helps you choose models instead of copying them blindly.

---

### Day 44

Topics:

* Localization vs detection
* One-stage vs two-stage detectors
* R-CNN, Fast/Faster R-CNN, SSD, YOLO, DETR
* IoU and mAP

Project/Task:

* Detection Concepts + Dataset Prep

Deliverable:

* Prepare or annotate a small detection dataset
* Notes on detection evolution

Practical outcome:

* Dataset and concept preparation for object detection.

Why this day matters:

* Detection requires bounding boxes and different evaluation thinking.

---

### Day 45

Topics:

* YOLO workflow
* Training and inference
* mAP

Project/Task:

* YOLO Detection Project (Part 1) - Portfolio Project 6

Deliverable:

* Train YOLO on a small dataset
* Run inference
* Report mAP/IoU

Practical outcome:

* A first object detection project.

Why this day matters:

* YOLO is widely used for practical real-time detection.

---

### Day 46

Topics:

* mAP/IoU deep dive
* Confidence and NMS thresholds
* Error analysis

Project/Task:

* YOLO Detection Project (Part 2)

Deliverable:

* Tune thresholds
* Analyze false positives and false negatives
* Save annotated output images

Practical outcome:

* A more credible object detection report.

Why this day matters:

* Detection quality depends on thresholds and error analysis.

---

### Day 47

Topics:

* Semantic, instance, and panoptic segmentation
* FCN, U-Net, Mask R-CNN, DeepLab, SAM
* Dice and IoU

Project/Task:

* Segmentation Concepts + Dataset Prep

Deliverable:

* Prepare a segmentation dataset
* Notes on segmentation evolution

Practical outcome:

* Preparation for segmentation modeling.

Why this day matters:

* Segmentation solves pixel-level problems that classification and detection cannot.

---

### Day 48

Topics:

* U-Net architecture
* Encoder-decoder
* Skip connections
* Segmentation training

Project/Task:

* U-Net Segmentation Project (Part 1) - Portfolio Project 7

Deliverable:

* Train U-Net
* Predict masks
* Compute Dice/IoU

Practical outcome:

* A beginner segmentation project.

Why this day matters:

* U-Net is a common baseline for medical, satellite, and mask-based segmentation tasks.

---

### Day 49

Topics:

* Mask quality analysis
* Augmentation for segmentation
* Pretrained backbones and SAM idea

Project/Task:

* U-Net Segmentation Project (Part 2)

Deliverable:

* Improve masks
* Compare backbones where practical
* Save prediction overlays

Practical outcome:

* Visual segmentation results suitable for a portfolio.

Why this day matters:

* Segmentation projects need visual evidence, not only metric numbers.

---

### Day 50

Topics:

* Image-input API
* Streamlit image demo
* Inference basics

Project/Task:

* CV Model Serving

Deliverable:

* Serve one CV model through an API and simple UI
* Test with sample images

Practical outcome:

* A demo path for one CV project.

Why this day matters:

* Serving turns a model into an app reviewers can inspect.

---

### Day 51

Topics:

* CV documentation
* Limitations
* Interview prep

Project/Task:

* CV Finalization + Interview Pack

Deliverable:

* README for the strongest CV project
* Example outputs
* Interview answers and resume bullets

Practical outcome:

* CV work becomes portfolio-ready and interview-ready.

Why this day matters:

* CV interview questions often focus on metrics, architectures, and task differences.

---

## Phase 6: Natural Language Processing (Days 52-61)

Follow the evolution that leads into transformers: representations -> RNN -> LSTM/GRU -> seq2seq -> attention.

### Day 52

Topics:

* Tokenization
* Stemming and lemmatization
* Stop words
* N-grams
* NLP task landscape

Project/Task:

* NLP Preprocessing Notebook

Deliverable:

* Preprocess a text corpus
* One-page map of NLP tasks and metrics

Practical outcome:

* A clean starting point for NLP projects.

Why this day matters:

* Text needs careful preprocessing before modeling.

---

### Day 53

Topics:

* Bag of Words
* TF-IDF
* Word2Vec, GloVe, fastText
* Counts to meaning

Project/Task:

* Representations Comparison

Deliverable:

* Vectorize text three ways
* Visualize or inspect nearest words

Practical outcome:

* A comparison of classical text representations.

Why this day matters:

* NLP representation choices shape model behavior.

---

### Day 54

Topics:

* Text classification
* Sentiment
* NER
* TF-IDF plus classical models

Project/Task:

* NLP Text Classification (Portfolio Project 8)

Deliverable:

* Train a text classifier
* Evaluate precision, recall, and F1
* Add a sentiment example

Practical outcome:

* A practical NLP portfolio project.

Why this day matters:

* Text classification is a common real-world NLP task.

---

### Day 55

Topics:

* Why order matters
* RNN
* Long-range dependency
* Vanishing gradients

Project/Task:

* RNN Text Model

Deliverable:

* Build an RNN for classification or generation
* Observe its limits

Practical outcome:

* A concrete view of why RNNs were useful and limited.

Why this day matters:

* Understanding RNN limits makes attention and transformers easier.

---

### Day 56

Topics:

* LSTM gates
* GRU
* When to use which

Project/Task:

* LSTM/GRU Upgrade

Deliverable:

* Replace RNN with LSTM/GRU
* Compare and explain the gain

Practical outcome:

* A model evolution comparison for sequence learning.

Why this day matters:

* LSTM and GRU fix parts of the long-term memory problem.

---

### Day 57

Topics:

* Encoder-decoder
* Translation, summarization, captioning
* Fixed-vector bottleneck

Project/Task:

* Seq2Seq Mini-Project

Deliverable:

* Build a toy seq2seq task
* Observe the bottleneck

Practical outcome:

* A bridge from RNNs to attention.

Why this day matters:

* Seq2Seq shows the architecture problem attention was built to solve.

---

### Day 58

Topics:

* Attention mechanism
* Alignment
* Leap toward transformers

Project/Task:

* Add Attention

Deliverable:

* Add attention to seq2seq
* Compare with and without attention
* Visualize attention weights

Practical outcome:

* Attention becomes a working concept, not only theory.

Why this day matters:

* Attention is the core idea behind transformers.

---

### Day 59

Topics:

* NLP capability evolution
* Image captioning
* Multimodal idea

Project/Task:

* Captioning / Evolution Notes

Deliverable:

* Short evolution timeline
* Small captioning demo or notes

Practical outcome:

* A conceptual bridge between CV and NLP.

Why this day matters:

* Modern AI increasingly combines vision, text, and structured context.

---

### Day 60

Topics:

* F1
* BLEU
* ROUGE
* Perplexity
* Exact-match/F1 for QA

Project/Task:

* NLP Evaluation Report

Deliverable:

* Evaluate NLP models with correct metrics
* Document trade-offs

Practical outcome:

* A metrics-aware NLP project.

Why this day matters:

* NLP tasks require task-specific metrics.

---

### Day 61

Topics:

* NLP documentation
* Limitations
* Interview prep

Project/Task:

* NLP Finalization + Interview Pack

Deliverable:

* README for strongest NLP project
* Interview answers and resume bullets

Practical outcome:

* NLP work becomes portfolio-ready and interview-ready.

Why this day matters:

* NLP fundamentals support LLM and RAG work.

---

## Phase 7: Transformers & Generative AI / LLMs (Days 62-74)

The core of modern AI: transformer architecture, model families, prompting, APIs, tools, and RAG.

### Day 62

Topics:

* Self-attention
* Q/K/V
* Scaled dot-product attention
* Multi-head attention

Project/Task:

* Transformer Deep-Dive Notes (Part 1)

Deliverable:

* Explain Q/K/V and multi-head attention
* Small attention computation
* Read and summarize key ideas from "Attention Is All You Need"

Practical outcome:

* A clear explanation of transformer attention.

Why this day matters:

* Self-attention is the mechanism behind modern LLMs.

---

### Day 63

Topics:

* Positional encoding
* Encoder/decoder blocks
* Feed-forward layers
* Residuals and layer norm
* Parallelization advantage

Project/Task:

* Transformer Block Walkthrough (Part 2)

Deliverable:

* Diagram and notes of a transformer block
* Explain why transformers parallelize better than RNNs

Practical outcome:

* A model-level understanding of transformer architecture.

Why this day matters:

* LLM usage is stronger when the architecture is not a black box.

---

### Day 64

Topics:

* Encoder-only models such as BERT
* Decoder-only models such as GPT
* Encoder-decoder models such as BART/T5

Project/Task:

* Families Comparison + BERT Fine-tune

Deliverable:

* Comparison table of model families
* Fine-tune BERT or DistilBERT for classification

Practical outcome:

* A practical transformer classification project.

Why this day matters:

* Different transformer families solve different task types.

---

### Day 65

Topics:

* BERT embeddings
* Sentence transformers
* Classification or NER
* Hugging Face basics

Project/Task:

* Transformer NLP Project

Deliverable:

* Build classifier or NER model with Hugging Face
* Compare with classical NLP baseline

Practical outcome:

* A transformer-based NLP improvement over earlier methods.

Why this day matters:

* Hugging Face is a core tool in modern NLP and LLM workflows.

---

### Day 66

Topics:

* Causal language modeling
* Greedy, beam, top-k, top-p, temperature
* Generation control

Project/Task:

* Text Generation Lab

Deliverable:

* Generate text with a decoder model
* Compare decoding strategies

Practical outcome:

* A controlled text generation experiment.

Why this day matters:

* Decoding strategy changes output quality, creativity, and reliability.

---

### Day 67

Topics:

* Scaling laws
* Pretraining, instruction tuning, RLHF
* BPE tokenization
* Context windows

Project/Task:

* LLM Training-Stages Notes

Deliverable:

* Explain pretraining -> SFT -> RLHF
* Notes on context window cost

Practical outcome:

* A realistic mental model of how LLMs are trained and used.

Why this day matters:

* AI engineers need to know where model behavior comes from.

---

### Day 68

Topics:

* Open vs closed models
* API usage
* Environment variables
* Errors, cost, and latency

Project/Task:

* AI API Starter App

Deliverable:

* Call an LLM API safely
* Use environment variables
* Compare small vs large model on one task

Practical outcome:

* A safe API integration pattern.

Why this day matters:

* API-based LLM work is common in AI engineering roles.

---

### Day 69

Topics:

* Zero-shot and few-shot prompting
* System prompts
* Structured output
* Prompt evaluation and versioning

Project/Task:

* Prompt Evaluation Lab

Deliverable:

* Compare prompt strategies on a small test set
* Track outputs
* Document improvements

Practical outcome:

* A repeatable prompt testing workflow.

Why this day matters:

* Prompting should be evaluated, not guessed.

---

### Day 70

Topics:

* JSON/schema-constrained output
* Response parsing and validation
* Function/tool calling

Project/Task:

* Structured Output + Tool Calling Demo

Deliverable:

* Get validated JSON
* Define and route to a tool
* Handle malformed responses

Practical outcome:

* A bridge from LLM responses to app behavior.

Why this day matters:

* Tool calling is the gateway from chatbots to agents.

---

### Day 71

Topics:

* Embeddings for search
* Vector similarity
* Chunking strategies
* Vector databases

Project/Task:

* Semantic Search + Vector Store

Deliverable:

* Embed and chunk documents
* Store in vector database
* Retrieve with metadata

Practical outcome:

* A semantic search foundation for RAG.

Why this day matters:

* RAG depends on finding the right context before generation.

---

### Day 72

Topics:

* Retrieval
* Context injection
* Source-aware answers
* Hallucination reduction

Project/Task:

* RAG Document Assistant (Portfolio Project 9, Part 1)

Deliverable:

* Connect retrieval to generation
* Answer using retrieved context
* Show sources or citations

Practical outcome:

* Start a practical RAG assistant.

Why this day matters:

* RAG is one of the most useful production patterns for LLM apps.

---

### Day 73

Topics:

* Hybrid search
* Query rewriting
* Reranking
* RAG evaluation

Project/Task:

* RAG Assistant (Part 2) + Evaluation

Deliverable:

* Add reranking or hybrid search
* Build eval question set
* Measure and improve weak cases

Practical outcome:

* A tested RAG system, not only a demo.

Why this day matters:

* RAG quality depends on retrieval and evaluation.

---

### Day 74

Topics:

* Streamlit chat UI with sources
* FastAPI RAG endpoint
* Generative AI interview prep

Project/Task:

* RAG App UI + API + Gen AI Interview Pack

Deliverable:

* Chat UI with answer and sources
* FastAPI endpoint returning answer, sources, and status
* Interview answers and resume bullets

Practical outcome:

* Portfolio-ready RAG app with UI and API.

Why this day matters:

* A RAG assistant becomes much stronger when users can interact with it.

---

## Phase 8: Fine-tuning, Quantization & Serving (Days 75-80)

Learn when to prompt, when to use RAG, when to fine-tune, and how to serve models efficiently.

### Day 75

Topics:

* Prompt vs RAG vs fine-tuning
* Full fine-tuning vs PEFT
* Data requirements

Project/Task:

* Adaptation Decision Notes

Deliverable:

* Decision tree for prompt -> RAG -> fine-tune -> quantize/serve
* Identify a fine-tune-worthy task

Practical outcome:

* A practical decision guide for adapting LLMs.

Why this day matters:

* Fine-tuning is not always the right solution.

---

### Day 76

Topics:

* PEFT
* LoRA
* QLoRA
* Adapters

Project/Task:

* PEFT Concepts + Setup

Deliverable:

* Notes on LoRA/QLoRA mechanics
* Environment setup for a fine-tuning stack

Practical outcome:

* Ready environment and notes for parameter-efficient fine-tuning.

Why this day matters:

* PEFT makes fine-tuning more affordable for learners and smaller hardware.

---

### Day 77

Topics:

* Instruction dataset formatting
* Training
* Overfitting on small data

Project/Task:

* QLoRA Fine-Tuning Project (Part 1) - Portfolio Project 10

Deliverable:

* Prepare instruction dataset
* QLoRA fine-tune a small model
* Save adapters

Practical outcome:

* First fine-tuned LLM learning lab.

Why this day matters:

* Fine-tuning requires clean data formatting and careful expectations.

---

### Day 78

Topics:

* Before/after comparison
* Evaluation sets
* Fine-tuning gains and failures

Project/Task:

* Fine-Tuning Project (Part 2)

Deliverable:

* Compare base vs fine-tuned model
* Document gains and failure cases

Practical outcome:

* Evidence-based fine-tuning evaluation.

Why this day matters:

* Fine-tuning without evaluation can make a model worse.

---

### Day 79

Topics:

* Quantization
* GPTQ, AWQ, bitsandbytes, GGUF
* Size/speed/quality trade-off

Project/Task:

* Quantization Experiment

Deliverable:

* Quantize a model
* Compare size, speed, and quality vs full precision

Practical outcome:

* A practical understanding of model compression.

Why this day matters:

* Serving models often requires trade-offs between cost, latency, and quality.

---

### Day 80

Topics:

* vLLM, TGI, Ollama
* KV-cache and batching
* Latency and cost
* Interview prep

Project/Task:

* Local LLM Serving + Interview Pack

Deliverable:

* Serve a quantized model locally where practical
* Measure latency
* Interview answers and resume bullets

Practical outcome:

* Basic model serving awareness for LLM systems.

Why this day matters:

* AI engineers need to think about serving and cost, not only model quality.

---

## Phase 9: Agents & Agentic AI (Days 81-91)

Move from a model that answers to a system that plans, uses tools, remembers, and self-corrects.

### Day 81

Topics:

* What makes a system agentic
* Agent loop
* Agent vs plain LLM

Project/Task:

* Agent Concepts Notes

Deliverable:

* Explain reason -> plan -> act -> observe -> adjust
* Map a task to the loop
* Notes on tool use

Practical outcome:

* Clear conceptual base for agentic AI.

Why this day matters:

* Agents are systems, not only prompts.

---

### Day 82

Topics:

* Function/tool calling recap
* ReAct
* Planning patterns

Project/Task:

* ReAct Tool-Using Agent (Single Tool)

Deliverable:

* Agent that reasons, calls one tool, observes, and responds
* Document failure cases

Practical outcome:

* First agentic workflow.

Why this day matters:

* ReAct connects reasoning and action in a simple pattern.

---

### Day 83

Topics:

* Short-term memory
* Long-term memory
* State persistence

Project/Task:

* Agent with Memory

Deliverable:

* Add short- and long-term memory
* Persist state across turns

Practical outcome:

* A more useful assistant that remembers context.

Why this day matters:

* Memory changes an agent from stateless chat to workflow support.

---

### Day 84

Topics:

* Multi-tool agents
* Tool routing
* Robust tool design
* Error recovery

Project/Task:

* Multi-Tool Agent (Portfolio Project 11, Part 1)

Deliverable:

* Agent using 2-3 tools
* Retries and error handling

Practical outcome:

* A practical multi-tool agent system.

Why this day matters:

* Tool routing is core to real agentic apps.

---

### Day 85

Topics:

* LangGraph
* CrewAI
* OpenAI Agents SDK
* Claude Agent SDK
* Smolagents
* Google ADK
* Framework selection

Project/Task:

* Framework Selection + Rebuild

Deliverable:

* Rebuild agent in LangGraph or CrewAI
* Notes on why the framework was chosen

Practical outcome:

* A framework-based version of the agent.

Why this day matters:

* Framework choice should match the use case, not hype.

---

### Day 86

Topics:

* Roles and delegation
* Planner / worker / reviewer
* Debate and consensus
* When multi-agent helps or hurts

Project/Task:

* Multi-Agent Workflow (Project 11, Part 2)

Deliverable:

* Planner + worker + reviewer workflow on a real task

Practical outcome:

* A realistic multi-agent pattern with clear roles.

Why this day matters:

* Multi-agent systems add complexity and should be justified.

---

### Day 87

Topics:

* Longer-horizon autonomy
* Graphs and state machines
* Human-in-the-loop
* Checkpoints and rollback

Project/Task:

* Orchestrated Agent

Deliverable:

* Add human-in-the-loop and checkpointing
* Handle a multi-step autonomous task

Practical outcome:

* A safer agent workflow with control points.

Why this day matters:

* Autonomy needs guardrails and review, especially for multi-step tasks.

---

### Day 88

Topics:

* MCP basics
* Tool/data connections
* Agent-to-agent communication concepts
* Why standards matter

Project/Task:

* MCP Integration

Deliverable:

* Connect agent to a tool or data source through MCP where practical
* If not practical, build a minimal integration and document MCP notes

Practical outcome:

* Exposure to emerging agent-tool standards.

Why this day matters:

* Standards like MCP can make tools and agents easier to connect.

---

### Day 89

Topics:

* Guardrails and validation
* Tracing and observability
* Cost control
* Prompt injection defense
* Tool permissions and sandboxing

Project/Task:

* Hardened Agent

Deliverable:

* Add guardrails and tracing
* Add prompt-injection defense check
* Document cost and permission limits

Practical outcome:

* A safer and more observable agent.

Why this day matters:

* Agentic systems need safety and monitoring, not only capability.

---

### Day 90

Topics:

* Task success rate
* Tool-call correctness
* Trajectory evaluation
* Regression tests for agents

Project/Task:

* Agent Evaluation Report

Deliverable:

* Define success metrics
* Build test set
* Measure and improve

Practical outcome:

* A measurable agent system.

Why this day matters:

* Agents should be evaluated by task success and tool behavior, not only answer quality.

---

### Day 91

Topics:

* Documentation and architecture diagram
* Demo
* Interview prep

Project/Task:

* Agentic AI Finalization (Project 11) + Interview Pack

Deliverable:

* README with architecture, tools, memory, guardrails, and evaluation
* Demo
* Interview answers and resume bullets

Practical outcome:

* Agentic AI project becomes portfolio-ready.

Why this day matters:

* Agent systems need architecture explanation more than simple scripts do.

---

## Phase 10: Capstone, Portfolio & Interviews (Days 92-100)

Turn the roadmap into one flagship project plus a hireable portfolio.

### Day 92

Topics:

* Problem definition
* Users
* Success metrics
* Scope

Project/Task:

* Final Capstone Plan

Deliverable:

* Choose capstone in strongest track
* Define users, data, workflow, success metrics, and checklist

Practical outcome:

* A scoped capstone that can be finished.

Why this day matters:

* Capstones fail when the problem and success criteria are vague.

---

### Day 93

Topics:

* Data/document preparation
* EDA or inspection
* Baseline build

Project/Task:

* Capstone Data + Baseline

Deliverable:

* Prepare data
* Run EDA or document inspection
* Build first working baseline and save results

Practical outcome:

* A working capstone baseline.

Why this day matters:

* A baseline creates something real to improve.

---

### Day 94

Topics:

* Core build
* Evaluation and error analysis
* Iteration

Project/Task:

* Capstone Improvement Pass

Deliverable:

* Improve model, RAG, or agent
* Compare before and after
* Document limitations

Practical outcome:

* Measurable progress beyond the baseline.

Why this day matters:

* Strong projects show iteration, not only a first attempt.

---

### Day 95

Topics:

* UI
* FastAPI endpoint
* Integration

Project/Task:

* Capstone App Layer

Deliverable:

* Build UI and API with clear inputs/outputs
* Save screenshots

Practical outcome:

* A demo-friendly app around the capstone.

Why this day matters:

* UI/API work makes the capstone easier to review and share.

---

### Day 96

Topics:

* Docker and reproducibility
* Deploy or recorded demo

Project/Task:

* Capstone Deployment

Deliverable:

* Dockerize where practical
* Deploy or record demo
* Document setup and run commands

Practical outcome:

* A reproducible capstone demo path.

Why this day matters:

* Deployment evidence is valuable even when it is simple.

---

### Day 97

Topics:

* Final README
* Architecture
* Results
* Limitations
* Next steps

Project/Task:

* Capstone Documentation Finalization

Deliverable:

* Complete capstone README
* Architecture diagram
* Setup, usage, results, limitations, and demo links

Practical outcome:

* A polished flagship project page.

Why this day matters:

* Documentation turns a technical build into a portfolio asset.

---

### Day 98

Topics:

* GitHub/README polish
* Project pinning
* Resume bullets
* LinkedIn positioning

Project/Task:

* Portfolio + Resume + LinkedIn Update

Deliverable:

* Polish root README
* Pin strongest projects
* Resume bullets for 6-8 projects
* LinkedIn showcase post outline

Practical outcome:

* Portfolio work becomes job-search ready.

Why this day matters:

* Good projects need clear presentation to create opportunities.

---

### Day 99

Topics:

* ML/DL/CV/NLP/Gen AI/Agents recap
* Project storytelling
* Mock interview

Project/Task:

* Full Technical Mock Interview

Deliverable:

* Concise answers across all domains
* Practice explaining 3 flagship projects
* Identify final weak topics

Practical outcome:

* Interview readiness connected to actual work.

Why this day matters:

* Interviews test communication and judgment as much as code.

---

### Day 100

Topics:

* Final reflection
* Career readiness
* Public showcase
* Specialization choice

Project/Task:

* Final Portfolio Showcase

Deliverable:

* Publish final GitHub review and LinkedIn post
* Summarize skills, projects, strengths, and next steps
* Pick a specialization to go deeper

Practical outcome:

* A complete public learning record and portfolio direction.

Why this day matters:

* The final day turns daily execution into a professional story.

---

## Evaluation & Metrics Reference

Learn these once around Day 20 and reuse them across the whole roadmap.

Classification:

* Accuracy: useful but misleading on imbalanced data.
* Precision: important when false positives are costly.
* Recall: important when false negatives are costly.
* F1: useful for imbalanced data.
* ROC-AUC / PR-AUC: ranking quality; PR-AUC is better for heavy imbalance.
* Confusion matrix: raw breakdown of prediction outcomes.

Regression:

* MAE: error in target units and easier to explain.
* MSE/RMSE: penalizes large errors; RMSE is in target units.
* R2: variance explained.

Clustering:

* Silhouette score.
* Inertia / elbow method.
* Davies-Bouldin score.

Computer Vision:

* IoU: box or mask overlap.
* mAP: object detection standard.
* Dice: segmentation overlap.

NLP:

* F1: classification and QA overlap.
* BLEU: translation.
* ROUGE: summarization.
* Perplexity: language model quality; lower is better.
* Exact match: QA correctness.

RAG / LLM / Agents:

* RAG: faithfulness, context precision/recall, answer quality.
* LLM: task eval sets, human/LLM-as-judge, hallucination rate.
* Agents: task success rate, tool-call correctness, trajectory/steps, cost per task.

---

## Final Day 100 Deliverables

By Day 100, the repository should contain:

* EDA + SQL Business Analytics
* End-to-End Supervised ML
* Customer Segmentation / Clustering
* Deep Learning Classifier
* Image Classification
* Object Detection
* Image Segmentation
* NLP Text Classification
* RAG Document Assistant
* QLoRA Fine-Tuned Model
* Agentic AI System
* Flagship Capstone
* Clean GitHub navigation with strong READMEs
* 2-3 deployed or recorded demos
* Evaluation & Metrics reference
* Resume bullets and LinkedIn positioning
* Interview notes for ML, DL, CV, NLP, Gen AI, and Agentic AI

Realistic note:

* Not every project needs to be equally polished. The strongest 4-6 projects should become flagship portfolio projects. The rest can remain learning labs.

---

## Phase Milestones

Phase 2 (Days 15-24):

* Output: SQL analytics plus end-to-end supervised ML project.
* Interview focus: leakage, precision/recall/F1, bias-variance, boosting vs bagging, feature importance.

Phase 3 (Days 25-30):

* Output: segmentation/clustering project, ML app, prediction API.
* Interview focus: clustering, PCA, imbalance, API design, reproducibility.

Phase 4 (Days 31-40):

* Output: MNIST MLP, CNN classifier, tracked run.
* Interview focus: autograd, backprop, optimizers, overfitting, BatchNorm.

Phase 5 (Days 41-51):

* Output: classifier, detector, segmentation project, served CV model.
* Interview focus: IoU vs mAP, one-stage vs two-stage, semantic vs instance segmentation, ResNet skip connections.

Phase 6 (Days 52-61):

* Output: text classifier, RNN/LSTM model, seq2seq + attention.
* Interview focus: embeddings, RNN vs LSTM vs GRU, attention, BLEU/ROUGE/perplexity.

Phase 7 (Days 62-74):

* Output: BERT fine-tune, generation lab, RAG assistant with UI/API.
* Interview focus: self-attention, encoder vs decoder, RLHF, decoding, RAG vs prompting.

Phase 8 (Days 75-80):

* Output: QLoRA model with evaluation, quantization experiment, local serving.
* Interview focus: LoRA/QLoRA, quantization trade-offs, serving, when to fine-tune vs RAG.

Phase 9 (Days 81-91):

* Output: ReAct agent, multi-tool agent, multi-agent workflow, MCP integration, hardened agent.
* Interview focus: agent loop, ReAct, memory types, single vs multi-agent, agent evaluation, prompt injection, MCP.

Phase 10 (Days 92-100):

* Output: capstone with UI/API/deployment, polished portfolio, interview notes.
* Interview focus: all domains plus career direction.

---

## Rules For Codex

1. Always read `roadmap.md` and `day-plans.md` first when available.
2. If `day-plans.md` exists, it must follow this mentor-reviewed Python to Agentic AI roadmap.
3. Focus on the current day unless asked to review or update the roadmap.
4. Teach concepts before coding.
5. Encourage project-based learning.
6. Help create portfolio-quality deliverables.
7. Do not skip prerequisites from earlier days.
