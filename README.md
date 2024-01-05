# Link-LLMs-ProofofConcept
Try out and use available algorithms such as Llama and Mistral7b in practice

1. Project Requirements:
    a. Download the Pubmed data, unpack it, and extract the relevant information.
    b. Design and implement an expert system that can answer questions based on the Pubmed abstracts.
    c. Test the system with sample queries to ensure it meets the project objectives

2. Data Source and Data Structure

    Data Source:
     PubMed contains citations and abstracts of biomedical literature from several NLM literature resources, including MEDLINE—the largest component of the PubMed database.

     Download PubMed Data: https://ftp.ncbi.nlm.nih.gov/pubmed/baseline/

    Data Structure:
        PMID
        Title
        ArticleTitle
        Abstract
        Journal-PubDate
        MeshHeadingList

3. Explore Available Methods and tools
    Hugging Face Transformers
    spaCy
    NLTK

    Choose models that are pre-trained on life science or biomedical data:

        BioBERT:A biomedical language representation model pre-trained on large-scale biomedical corpora. It's based on the BERT architecture.

        SciBERT:Similar to BioBERT, SciBERT is a BERT-based model specifically trained on scientific text, including biomedical literature.

        ClinicalBERT:Tailored for clinical text, ClinicalBERT is designed to understand the specific language used in clinical notes and medical records.

        BlueBERT:Pre-trained on a large corpus containing both clinical and biomedical text, BlueBERT is another option for tasks related to life sciences.

        BERTology models (e.g., PubMedBERT):Some models are trained on PubMed abstracts and articles. PubMedBERT, for example, focuses on understanding the language used in PubMed publications.

    Some general algorithms and models commonly used in NLP and machine learning tasks: (which we can condiser for our project)

    Transformer Models:
        BERT (Bidirectional Encoder Representations from Transformers)
        GPT (Generative Pre-trained Transformer)
        RoBERTa (Robustly optimized BERT approach)
        T5 (Text-to-Text Transfer Transformer)

    Sequence-to-Sequence Models:
        LSTM (Long Short-Term Memory)
        GRU (Gated Recurrent Unit)
        Seq2Seq with Attention Mechanism

    Named Entity Recognition (NER) Models:
        SpaCy NER models
        BioBERT for biomedical NER

    Information Retrieval Models:
        Elasticsearch (for indexing and searching relevant documents)
        BM25 (Best Matching 25) for document ranking

    Summarization Models:
        Pointer-Generator Networks
        Extractive Summarization models (e.g., using TF-IDF)

    Question Answering Models:
        T5 for question answering
        BERT-based models fine-tuned for QA tasks

    Rule-Based Systems:
        Define custom rules for specific tasks, like extracting information about genes, organisms, diseases, drugs, etc.

    Clustering Algorithms:
        K-means clustering for grouping similar documents

    Deep Learning Architectures for Document Understanding:
        Doc2Vec for document embeddings
        Paragraph Vectors for context understanding

    Topic Modeling:
        Latent Dirichlet Allocation (LDA) for identifying topics in a collection of documents.

## HOW TO USE

Navigate into this directory:
1.Create and activate a Python virtual environment
    $ python -m venv venv
    On Windows:
    $ source venv/Scripts/activate
    On macOS/Linux:
    $ source venv/bin/activate

2.Update pip and install the required dependencies:
    (venv) $ python.exe -m pip install --upgrade pip
    (venv) $ pip install Flask
    (venv) $ pip install transformers
    (venv) $ pip install pandas
    # install PyTorch
    (venv) $ pip install torch   [or]   $ pip3 install torch torchvision torchaudio

3.Start the Flask server:
    (venv) $ python main.py
