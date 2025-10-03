# %%

# =============================================================================
# Make a summary
# =============================================================================

from LLMlight import LLMlight

client = LLMlight(model='mistralai/mistral-small-3.2', top_chunks=5)

# Add multiple PDF files to the database
url = 'https://proceedings.neurips.cc/paper_files/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf'
pdf_text = client.read_pdf(url)


summary_text = client.summarize(context=pdf_text)

# %%
# New example

from LLMlight import LLMlight

client = LLMlight(model='mistralai/mistral-small-3.2')
client.memory_init(file_path='knowledge_base.mp4')

# Add a PDF file to the memory (extracts and chunks text automatically)
client.memory_add(files='https://erdogant.github.io/publications/papers/2020%20-%20Taskesen%20et%20al%20-%20HNet%20Hypergeometric%20Networks.pdf')
client.memory_save()

# Query on the new knowledge
response = client.prompt('Summarize the document.')
print(response)


# %%

# =============================================================================
# REPRODUCIBILITY
# =============================================================================
# Load library
from LLMlight import LLMlight

# Initialize with default settings
client = LLMlight(model='mistralai/mistral-small-3.2')

# Add multiple PDF files to the database
url = 'https://proceedings.neurips.cc/paper_files/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf'
pdf_text = client.read_pdf(url)

# Create response
responses = []
for temp in [0.99, 0.99, 0.99, 0.99, 0.99, 0.1, 0.1, 0.1, 0.1, 0.1]:
    response = client.prompt('Summarize how layers are used in an attention network in combination to the increasing complexity.',
                             context=pdf_text,
                             instructions='You are a helpfull assistant. Keep your answer brief.',
                             temperature=temp,
                             )
    
    responses.append(response)



# %%


# Load library
from LLMlight import LLMlight

# Initialize
client = LLMlight(model='mistralai/mistral-small-3.2', file_path='local_database.mp4', context_strategy=None)
# Make a prompt
response = client.prompt('What are Graphical Hypergeometric Networks?', instructions='Answer the question using the information from the context.')
print(response)

# Initialize
client = LLMlight(model='mistralai/mistral-small-3.2', file_path='local_database.mp4', context_strategy='chunk-wise')
# Make a prompt
response = client.prompt('What are Graphical Hypergeometric Networks?', instructions='Answer the question using the information from the context.')
print(response)

# Initialize
client = LLMlight(model='mistralai/mistral-small-3.2', file_path='local_database.mp4', context_strategy='global-reasoning')
# Make a prompt
response = client.prompt('What are Graphical Hypergeometric Networks?', instructions='Answer the question using the information from the context.')
print(response)


# %%

# =============================================================================
# Store many pdf files
# =============================================================================
# Load library
from LLMlight import LLMlight

# Initialize with default settings
client = LLMlight(model='mistralai/mistral-small-3.2', file_path='local_database.mp4')

url1 = 'https://proceedings.neurips.cc/paper_files/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf'
url2 = 'https://erdogant.github.io/publications/papers/2020%20-%20Taskesen%20et%20al%20-%20HNet%20Hypergeometric%20Networks.pdf'

# Add multiple PDF files to the database
client.memory_add(files=[url1, url2])

# Add more chunks of information
client.memory_add(text=['Small chunk that is also added to the database.',
                        'The capital of France is Amsterdam.'],
                  overwrite=True)

# Add all file types from a directory
client.memory_add(dirpath='c:/my_documents/',
                  filetypes = ['.pdf', '.txt', '.epub', '.md', '.doc', '.docx', '.rtf', '.html', '.htm'],
                  )

# Store to disk
client.memory_save()


# =============================================================================
# Load from database
# =============================================================================

# Import
from LLMlight import LLMlight
# Initialize with local database
client = LLMlight(model='mistralai/mistral-small-3.2', file_path='local_database.mp4')

# Get the top 5 chunks
client.memory_chunks(n=5)

# Search through the chunks using a query
out1 = client.memory.retriever.search('Attention Is All You Need', top_k=3)
out2 = client.memory.retriever.search('Enrichment analysis, Hypergeometric Networks', top_k=3)
out3 = client.memory.retriever.search('Capital of Amsterdam', top_k=3)

# [07-09-2025 21:31:51] [memory] [INFO] Downloading file from url..
# [07-09-2025 21:31:54] [memory] [INFO] Downloading file from url..
# [07-09-2025 21:31:54] [memory] [INFO] Adding 2 into memory.
# [07-09-2025 21:31:54] [memvid.encoder] [INFO] Extracting text from 11 pages of 3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf
# [07-09-2025 21:31:54] [memvid.encoder] [INFO] Added 85 chunks. Total: 85
# [07-09-2025 21:31:54] [memvid.encoder] [INFO] Added PDF content: 32567 characters from 3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf
# [07-09-2025 21:31:54] [memory] [INFO] Added to memory: 3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf
# [07-09-2025 21:31:54] [memvid.encoder] [INFO] Extracting text from 6 pages of 2020%20-%20Taskesen%20et%20al%20-%20HNet%20Hypergeometric%20Networks.pdf
# [07-09-2025 21:31:55] [memvid.encoder] [INFO] Added 73 chunks. Total: 158
# [07-09-2025 21:31:55] [memvid.encoder] [INFO] Added PDF content: 27757 characters from 2020%20-%20Taskesen%20et%20al%20-%20HNet%20Hypergeometric%20Networks.pdf
# [07-09-2025 21:31:55] [memory] [INFO] Added to memory: 2020%20-%20Taskesen%20et%20al%20-%20HNet%20Hypergeometric%20Networks.pdf

# [07-09-2025 21:32:45] [memory] [INFO] 🎬 Building video-memory: C:\Users\erdog\AppData\Local\Temp\temp_LLMlight\local_database.mp4
# [07-09-2025 21:32:45] [memory] [INFO] 📊 Total chunks to encode: 158
# [07-09-2025 21:32:45] [memvid.encoder] [INFO] Building video with 158 chunks using mp4v codec
# Generating QR frames: 100%|██████████| 158/158 [00:36<00:00,  4.30it/s]
# [07-09-2025 21:33:22] [memvid.encoder] [INFO] Generated 158 QR frames in C:\Users\erdog\AppData\Local\Temp\tmpso_pqflp\frames
# [07-09-2025 21:33:22] [memvid.encoder] [INFO] Encoding with OpenCV using mp4v codec...

# 🐛 FRAMES: 158 files in C:\Users\erdog\AppData\Local\Temp\tmpso_pqflp\frames
# Writing video frames: 100%|██████████| 158/158 [00:01<00:00, 144.29it/s]
# [07-09-2025 21:33:23] [memvid.encoder] [INFO] Building search index...
# [07-09-2025 21:33:23] [memvid.index] [INFO] Processing 158 chunks for indexing...
# [07-09-2025 21:33:23] [memvid.index] [INFO] Processing 158 valid chunks
# [07-09-2025 21:33:23] [memvid.index] [INFO] Generating embeddings for 158 chunks (full batch)
# [07-09-2025 21:33:24] [memvid.index] [INFO] ℹ️ Using Index (no training required)
# [07-09-2025 21:33:24] [memvid.index] [INFO] Successfully added 158 chunks to index
# [07-09-2025 21:33:24] [memvid.index] [INFO] Saved index to C:\Users\erdog\AppData\Local\Temp\temp_LLMlight\local_database
# [07-09-2025 21:33:24] [memvid.encoder] [INFO] Successfully built video: C:\Users\erdog\AppData\Local\Temp\temp_LLMlight\local_database.mp4
# [07-09-2025 21:33:24] [memvid.encoder] [INFO] Video duration: 10.5 seconds
# [07-09-2025 21:33:24] [memvid.encoder] [INFO] Video size: 2.5 MB

# [07-09-2025 21:33:24] [memory] [INFO] Added chunks are cleared.
# [07-09-2025 21:33:24] [sentence_transformers.SentenceTransformer] [INFO] Use pytorch device_name: cpu
# [07-09-2025 21:33:24] [sentence_transformers.SentenceTransformer] [INFO] Load pretrained SentenceTransformer: all-MiniLM-L6-v2
# [07-09-2025 21:33:26] [memvid.encoder] [INFO] Cleared all chunks
# [07-09-2025 21:33:26] [memory] [INFO] ✅ Video Memory saved to disk: C:\Users\erdog\AppData\Local\Temp\temp_LLMlight\local_database.mp4
# [07-09-2025 21:33:26] [memory] [INFO] ✅ Video file: 2.5 MB, containing 158 chunks

# [07-09-2025 21:33:26] [memory] [INFO] Loading memory:
# [07-09-2025 21:33:26] [memory] [INFO]   📁 Video: C:\Users\erdog\AppData\Local\Temp\temp_LLMlight\local_database.mp4
# [07-09-2025 21:33:26] [memory] [INFO]   📋 Index: C:\Users\erdog\AppData\Local\Temp\temp_LLMlight\local_database.json
# [07-09-2025 21:33:26] [sentence_transformers.SentenceTransformer] [INFO] Use pytorch device_name: cpu
# [07-09-2025 21:33:26] [sentence_transformers.SentenceTransformer] [INFO] Load pretrained SentenceTransformer: all-MiniLM-L6-v2
# [07-09-2025 21:33:27] [memvid.index] [INFO] Loaded index from C:\Users\erdog\AppData\Local\Temp\temp_LLMlight\local_database
# [07-09-2025 21:33:27] [memvid.retriever] [INFO] Video has 158 frames at 15.0 fps
# [07-09-2025 21:33:27] [memvid.retriever] [INFO] Initialized retriever with 158 chunks


# %%
# =============================================================================
# Import PDF as context WITH chunking
# =============================================================================

# Load library
from LLMlight import LLMlight

# Initialize with default settings
client = LLMlight(model='mistralai/mistral-small-3.2',
                  context_strategy='chunk-wise',
                  retrieval_method='naive_rag',
                  embedding={'memory': 'memvid', 'context': 'bert'},
                  top_chunks=5)

# Read pdf
path = 'https://proceedings.neurips.cc/paper_files/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf'
pdf_text = client.read_pdf(path, return_type='text')
context = pdf_text + '\n More text can be appended in this manner'

# Make a prompt
response = client.prompt('What is an attention network?',
                         context=context,
                         instructions='Answer the question using only the information from the context. If the answer can not be found, tell that.')

print(response)



# %%
# =============================================================================
# Import PDF as context
# =============================================================================

# Load library
from LLMlight import LLMlight

# Initialize with default settings
client = LLMlight(model='mistralai/mistral-small-3.2', context_strategy=None)

# Read pdf
path = 'https://proceedings.neurips.cc/paper_files/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf'
pdf_text = client.read_pdf(path, return_type='text')
context = pdf_text + '\n More text can be appended in this manner'

# Make a prompt
response = client.prompt('What is an attention network?',
                         context=context,
                         instructions='Answer the question using only the information from the context. If the answer can not be found, tell that.')


print(response)



# %% Add pdf to memory
from LLMlight import LLMlight
# Initialize with default settings
# client = LLMlight(model='microsoft/phi-4', file_path="knowledge_base.mp4", context_strategy=None)

# url = 'https://proceedings.neurips.cc/paper_files/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf'
# client.memory_add(files=url, overwrite=True)
# client.memory_save()
# client.memory_chunks(n=15)

# response = client.prompt('How many GPU were required?', instructions='Do not argue with the information in the context. Only return the information from the context. Keep your answer short.')
# print(response)

client = LLMlight(model='microsoft/phi-4', file_path="knowledge_base.mp4", context_strategy='global-reasoning')
client.memory_chunks(n=15)
response = client.prompt('Summarize the paper in 1 alinea', instructions='Only use the information from the context.')
print(response)


#%% No video memory usage
from LLMlight import LLMlight

# Initialize with default settings
client = LLMlight(model='microsoft/phi-4', file_path="knowledge_base.mp4", context_strategy=None)

# response = client.prompt('What is the capital of France?')
# print(response)

response = client.prompt('What is the capital of France?', context='The capital of France is Amsterdam.', instructions='Do not argue with the information in the context. Only return the information from the context. Keep your answer short.')
print(response)

response = client.prompt('What do apes like?', instructions='Answer with maximum of 3 words, and starts with "Apes like: "')
print(response)

response = client.prompt('Provide a summary of HyperSpectral.')
print(response)

# %%

from LLMlight import LLMlight

# Initialize the model
# client =  LLMlight(endpoint= "http://localhost:1234/v1/chat/completions")

# Validate the models and list only those the respond
# modelnames = client.get_available_models(validate=False)


# from memvid import MemvidEncoder, MemvidChat

# # Create video memory from text
# chunks = ["NASA founded 1958", "Apollo 11 landed 1969", "ISS launched 1998"]
# encoder = MemvidEncoder()
# encoder.add_chunks(chunks)
# encoder.build_video("space.mp4", "space_index.json")

# # Chat with your memory
# chat = MemvidChat("space.mp4", "space_index.json")
# response = chat.chat("When did humans land on the moon?")
# print(response)  # References Apollo 11 in 1969


#%% Load video memory, append and store in other file. Then check if info exists
from LLMlight import LLMlight

# Initialize with default settings
client = LLMlight(model='mistralai/mistral-small-3.2', retrieval_method=None, context_strategy=None, file_path='test.mp4')
client.memory_chunks(n=40)


# client.memory_load()
client.memory_chunks(n=40)

# Add chunks
client.memory_add(text=['Apes like USB sticks', 'The capital of France is Amsterdam.'])
client.memory_save()
client.memory_chunks(n=40)


client.memory_add(text=['test 123', 'lalala'], overwrite=True)
client.memory_save()
client.memory_chunks(n=40)

client.memory_add(text=['hiephoi'], overwrite=True)
client.memory_save()
client.memory_chunks(n=40)

client.memory_add(text=['What about this new line?'], overwrite=True)
client.memory_save()
client.memory_chunks(n=40)


client.memory_add(text=['123456789'], overwrite=True)
client.memory_save()
client.memory_chunks(n=40)

# Query
response = client.prompt('What is the capital of France?')

print(response)
response = client.prompt('What do Apes like?', instructions='Only use the context to retrieve your answer.')
print(response)

client.memory.show_stats()



response = client.prompt('The floor is what?',
                         context=context,
                         instructions='Answer the question using information from the context.')


#%% Import files into video memory
from LLMlight import LLMlight

dirpath = r'D:/pdf_files/'
# dirpath = r'D:\Users\Documents\Hack'

# Initialize with default settings
client = LLMlight()

# Load memory
client.memory_load(r'D:\REPOS\LLMlight\knowledge_base.mp4')

# Create new memory
client.memory_init(r'D:\REPOS\LLMlight\knowledge_base.mp4')

# Add dir recusrively
# client.memory_add(dirpath=dirpath, overwrite=True)
# Store memory to disk
# client.memory_save(overwrite=True)

# Query
response = client.prompt('Provide all relevant information about Samuel Christian Gobel')
print(response)

#%% Load video memory, append and store in other file. Then check if info exists
from LLMlight import LLMlight

# Initialize with default settings
client = LLMlight(retrieval_method=None, context_strategy=None, verbose='info')
# Create new memory
client.memory_init(file_path='knowledge_base_new.mp4')
# Add chunks
client.memory_add(text=['Apes like USB sticks', 'The capital of France is Amsterdam.'], overwrite=True)
# Store memory to disk
client.memory_save(overwrite=True)
# Query
response = client.prompt('What is the capital of France?')
print(response)
response = client.prompt('What do Apes like?')
print(response)

client.memory.show_stats()

#%% Load video memory, append and store in other file. Then check if info exists
from LLMlight import LLMlight

# Initialize with default settings
client = LLMlight(retrieval_method='knowledge_base_new.mp4', context_strategy=None)
# Query
response = client.prompt('What is the capital of France?')
print(response)
response = client.prompt('What do Apes like?')
print(response)



#%%
from LLMlight import LLMlight

# Initialize with default settings
client = LLMlight(retrieval_method=None, context_strategy='global-reasoning', top_chunks=10, chunks = {'method': 'chars', 'size': 1000, 'overlap': 200})
# Create new memory
client.memory_init(file_path='knowledge_base.mp4')
# Query
response = client.prompt('What is the Thesis Proposal of Samuel Christian Gobel, Burnout Classification')
print(response)





# Initialize with default settings
client = LLMlight(retrieval_method=None, context_strategy=None, file_path='knowledge_base.mp4')
# NEW chunks can NOT be added!
client.memory_add(text=['The floor is paper!'])
# Store memory to disk
client.memory_save(filepath="knowledge_base_new.mp4", overwrite=True)

# Test for the floor
response = client.prompt('The floor is what?', instructions='Do not argue with the information in the context. Only return the information from the context.')
print(response)
# Also test for Amsterdam
response = client.prompt('What is the capital of France?', instructions='Do not argue with the information in the context. Only return the information from the context.')
print(response)



#%% Append more text to previously created video memory but do not save
from LLMlight import LLMlight

# Initialize with default settings
client = LLMlight(retrieval_method="knowledge_base.mp4", context_strategy=None)

# Add chunks
filepath = r'D:\Users\Documents\Hack\Download and Visualize Land Surface Temperature and NDVI from Sentinel-3.pdf'
client.memory_add(input_files=filepath)

# Run a simple query
response = client.prompt('What is the capital of France?', context='The capital of France is Amsterdam.')
print(response)

response = client.prompt('What do apes like?', instructions='Answer with maximum of 3 words, and starts with "Apes like: "')
print(response)

response = client.prompt('Provide a summary of HyperSpectral.', instructions='Do not argue with the information in the context. Only return the information from the context.')
print(response)


#%% Re-use previous created video memory
from LLMlight import LLMlight

# Initialize with default settings
client = LLMlight(retrieval_method="knowledge_base.mp4", context_strategy=None)

# Run query
response = client.prompt('What do apes like?', instructions='Only return the information from the context. Answer with maximum of 3 words, and starts with "Apes like: "')
print(response)

response = client.prompt('What is the capital of France?', instructions='Do not argue with the information in the context. Only return the information from the context.')
print(response)


#%% Create new video memory and use it with prompting
from LLMlight import LLMlight

# Initialize with default settings
client = LLMlight(retrieval_method=None, context_strategy=None, verbose='info')

# Create new memory
client.memory_init()

# Add chunks
filepath = r'D:\Users\Documents\Hack\PCA on HyperSpectral Data. A Beginner friendly tutorial on… _ by Richa Dutt _ Towards Data Science.pdf'
client.memory_add(input_files=filepath)
client.memory_add(text=['Apes like USB sticks', 'The capital of France is Amsterdam.'])

# Build memory
client.memory_save(filepath="knowledge_base.mp4", overwrite=True)

response = client.prompt('What do apes like?', instructions='Only return the information from the context. Answer with maximum of 3 words, and starts with "Apes like: "')
print(response)

response = client.prompt('What is the capital of France?', instructions='Do not argue with the information in the context. Only return the information from the context.')
print(response)

response = client.prompt('Provide a summary of HyperSpectral.', instructions='Do not argue with the information in the context. Only return the information from the context.')
print(response)

# Run a simple query
# response = client.prompt('What is the capital of France?', context='The capital of France is Amsterdam.', instructions='Do not argue with the information in the context. Only return the information from the context.')
# print(response)



#%%
from memvid import MemvidEncoder, MemvidRetriever
import os

# Load documents
encoder = MemvidEncoder()
dirname = r'D:\Users\Documents\Hack'

# Add text files
for file in os.listdir(dirname):
    ext = os.path.split(file[-4:])[1]
    pathname = os.path.join(dirname, file)

    if ext == '.pdf':
        print(f'Adding: {file}')
        encoder.add_pdf(pathname, chunk_size=512, overlap=50)
    elif ext == '.txt':
        print(f'Adding: {file}')
        with open(pathname, "r") as f:
            encoder.add_text(f.read(), chunk_size=512, overlap=50)
    encoder.add_chunks('')
    # encoder.add_epub()

# Build optimized video
encoder.build_video(output_file="knowledge_base.mp4", index_file="knowledge_index.json")
# For maximum compression
# encoder.build_video(output_file="knowledge_base.mp4", index_file="knowledge_index.json", codec='h265')


# Initialize retriever
retriever = MemvidRetriever("knowledge_base.mp4", "knowledge_index.json")
query = 'Get something about pindakaas'
results = retriever.search(query, top_k=3)
search_results = retriever.index_manager.search(query, top_k=3)

for chunk in search_results:
    print(f"Score: {chunk[1]:.3f} | {chunk[2]['text'][:100]}...")


context='\n\n Chunk:'.join(results)

from LLMlight import LLMlight

# Initialize with default settings
client =  LLMlight(context_strategy=None, embedding=None, method=None)
client =  LLMlight()

default_system = """You are a helpful AI assistant with access to a knowledge base stored in video format. 

When answering questions:
1. Use the provided context from the knowledge base when relevant
2. Be clear about what information comes from the knowledge base vs. your general knowledge
3. If the context doesn't contain enough information, say so clearly
4. Provide helpful, accurate, and concise responses

The context will be provided with each query based on semantic similarity to the user's question."""

# Run a simple query
response = client.prompt('What should I do with pindakaas?', system=default_system, context=context)
print(response)


#%%
from memvid import MemvidEncoder, MemvidChat

# Create video memory from text chunks
chunks = ["Important fact 1", "Important fact 2", "Historical event details"]
encoder = MemvidEncoder()
encoder.add_chunks(chunks)
encoder.build_video("memory.mp4", "memory_index.json")

# Chat with your memory
chat = MemvidChat("memory.mp4", "memory_index.json", llm_provider='local', llm_api_key='http://localhost:1234/v1/chat/completions')
chat.start_session()
response = chat.chat("What do you know about historical events?")
print(response)
#%%
from LLMlight import LLMlight

# Initialize with default settings
client = LLMlight(embedding=None, context_strategy=None)

# Run a simple query
response = client.prompt('What is the capital of France?', system="You are a helpful assistant.")
print(response)

#%%
system = """Je bent een Nederlandse AI-assistent gespecialiseerd in het omzetten van
transcripties naar gestructureerde en overzichtelijke notulen. Jouw taak is om van een
transcriptie een professioneel verslag te maken, zelfs als de transcriptie afkomstig is
van automatische spraak-naar-tekst software en fouten kan bevatten. Je mag aannames maken
indien het de kwaliteit van de output zal verbeteren.
"""

query = """Je ontvangt een transcriptie van de gebruiker als input. Zet deze direct om in volledig
gestructureerde en gepolijste notulen volgens de bovenstaande richtlijnen.
Wanneer je klaar bent, geef je alleen het uiteindelijke verslag als output, zonder verdere uitleg.
"""

instructions = """Bij het verwerken van de transcriptie, houd je rekening met het volgende:
    1. **Corrigeren van fouten:** Je corrigeert duidelijke fouten in de transcriptie (zoals
    verkeerde woorden, grammaticale fouten en onduidelijke zinnen) op basis van de context.
    Als iets onzeker blijft, markeer je dit met '[?]'.
    2. **Heldere structuur:** Je formatteert de notulen volgens de volgende opbouw:
       - **Titel en datum van de bijeenkomst** (haal dit uit de context van de
       transcriptie, indien mogelijk, anders laat het leeg).
       - **Aanwezigen en afwezigen** (indien vermeld).
       - **Samenvatting:** Een beknopte samenvatting van de belangrijkste besproken
       onderwerpen en uitkomsten.
       - **Details per agendapunt:** Geef de belangrijkste punten en discussies weer per
       onderwerp.
       - **Actiepunten en besluiten:** Noteer actiepunten en besluiten genummerd en
       duidelijk geordend.
    3. **Samenvatten en structureren:** Behoud de kern van de informatie, verwijder
    irrelevante details en vermijd herhaling. Gebruik bondige, professionele taal.
    4. **Neutraliteit:** Schrijf in een objectieve, neutrale toon en geef geen subjectieve
    interpretaties.
    5. **Tijdsaanduidingen:** Voeg waar nodig tijdsaanduidingen toe om de volgorde van de
    bespreking te verduidelijken. Laat irrelevante tijdsaanduidingen weg.
    6. De context is in het Nederlands en de output zal jij ook schrijven in het Nederlands.
    """

context = "goedemorgen allemaal welkom bij de meeting over innovatie en llms fijn dat iedereen aanwezig is we willen vandaag stilstaan bij hoe we binnen onze organisatie deze technologie kunnen toepassen en wat daarbij komt kijken we zien dat er steeds meer interne vragen komen over gpt en andere taalmodellen dus het is goed om dit gezamenlijk te bespreken ja ik wil daar wel op inhaken want ik merk dat we bij de dataserviceafdeling regelmatig verzoeken krijgen van collega’s die iets met ai willen maar vaak niet precies weten wat llms zijn of wat ze kunnen doen precies en ik denk ook dat we het gesprek moeten voeren over waar de grens ligt van wat we wel en niet willen inzetten want er is een verschil tussen een leuke chatbot en een model dat echt beslissingen gaat nemen of beleidsvoorstellen genereert en daarbij komt ook nog dat veel van die modellen cloudgebaseerd zijn dus dat roept vragen op over gegevensbescherming en compliance want als we persoonsgegevens gebruiken in prompts dan zitten we al snel in het domein van de avg dat klopt en ik wil ook even benadrukken dat we niet alleen moeten kijken naar de risico’s maar ook naar de kansen want we hebben nu bijvoorbeeld een pilot lopen met een llm die interne documenten samenvat en dat bespaart mensen echt veel tijd ik kreeg vorige week nog feedback van een collega die zei dat ze nu in vijf minuten een samenvatting had van een rapport van veertig pagina’s ja dat is een goed voorbeeld en ook iets wat schaalbaar is mits we het goed inregelen dus dat vraagt om standaardisatie en ook wat governance hoe zorgen we ervoor dat niet iedereen zomaar een eigen api gaat gebruiken met gevoelige data ik denk dat we daarvoor moeten werken met een soort interne toolbox waarin modellen zitten die we al gescreend hebben op veiligheid en bruikbaarheid en dat mensen via die route aan de slag kunnen precies en dan komt de rol van ict ook om de hoek kijken want als we dit willen aanbieden moeten we ook nadenken over de infrastructuur draaien we lokaal of in de cloud hoeveel rekencapaciteit hebben we nodig en hoe monitoren we het gebruik en daarbij is het ook belangrijk dat we nadenken over training van medewerkers want het is niet vanzelfsprekend dat iedereen weet hoe je een goede prompt schrijft of wat je wel en niet moet doen met een taalmodel dat sluit aan bij het idee van een interne academy of leerlijn rond ai en llms waar je korte modules kunt volgen over ethiek techniek en praktische toepassing dat zou ik graag verder willen uitwerken misschien kunnen we dat koppelen aan de innovatieroute die we vorig jaar hebben opgestart daar zit al een structuur in waarin teams experimenten kunnen aanvragen en met begeleiding kleine pilots uitvoeren ja dat lijkt me een logische verbinding dan creëren we ook een kader waarin we experimenteren verantwoord maken dus met evaluatie ethische toetsing en duidelijke exitcriteria laten we dan afspreken dat we een werkgroep vormen die deze punten concretiseert ik stel voor dat we met z’n vijven alvast een conceptplan maken voor de directie en daar een voorstel in doen voor gefaseerde implementatie goed idee ik wil daar graag aan meedoen ik denk dat we het eerste concept binnen drie weken kunnen hebben als we de taken verdelen ik zal het format voor het voorstel aanleveren en dan kunnen we daarin opnemen wat de technische randvoorwaarden zijn plus de governanceprincipes dan stuur ik morgen even een datumprikker rond voor onze eerste werkgroepmeeting en dan kunnen we vanaf daar verder werken top dan sluiten we voor nu af dank allemaal voor jullie input en enthousiasme tot snel"

from LLMlight import LLMlight
modelname = 'deepseek-r1-0528-qwen3-8b'
modelname = 'hermes-3-llama-3.2-3b'

context_strategy='global-reasoning',
context_strategy='chunk-wise'

client =  LLMlight(modelname=modelname,
                 context_strategy=context_strategy,
                 method=None,
                 temperature=0.8,
                 top_p=1,
                 chunks={'type': 'chars', 'size': 8192, 'overlap': 2000},
                 n_ctx=16384,
                 verbose='debug',
                 )

# Run model
response = client.prompt(query,
                   instructions=instructions,
                   context=context,
                   system=system,
                   stream=False,
                   )
print(response)


#%%
# Run model
response2 = client.global_reasoning(query,
                   context=context,
                   instructions=instructions,
                   system=system,
                   return_per_chunk=False,
                   stream=False,
                   )
print(response2)

# Run model
response3 = client.chunk_wise(query,
                   context=context,
                   instructions=instructions,
                   system=system,
                   return_per_chunk=False,
                   stream=False,
                   )
print(response3)

# %%
from LLMlight import LLMlight
client =  LLMlight(verbose='debug')
client.check_logger()


#%% Available models
from LLMlight import LLMlight
client =  LLMlight(verbose='info')
modelnames = client.get_available_models(validate=False)

# %%
for modelname in modelnames:
    from LLMlight import LLMlight
    llm = LLMlight(modelname=modelname)
    print(llm.modelname)

    system_message = "You are a helpful assistant."
    response = llm.prompt('What is the capital of France?', system=system_message)
    print(response)

# %%
from LLMlight import LLMlight
model_path = r'C:/Users\beeld/.lmstudio/models/NousResearch/Hermes-3-Llama-3.2-3B-GGUF\Hermes-3-Llama-3.2-3B.Q4_K_M.gguf'
client =  LLMlight(endpoint=model_path, top_p=0.9)
# client.prompt('hello, who are you?')
system_message = "You are a helpful assistant."
response = client.prompt('What is the capital of France?', system=system_message)


#%%
import llama_cpp
print(llama_cpp.__version__)
print(llama_cpp.llama_cpp_version())  # Might crash if incompatible

# Check your GGUF model's metadata
model_path = r'C:/Users\beeld/.lmstudio/models/NousResearch/Hermes-3-Llama-3.2-3B-GGUF\Hermes-3-Llama-3.2-3B.Q4_K_M.gguf'
with open(model_path, 'rb') as f:
    header = f.read(128)
    print(header)


#%%
import os
import logging
import requests
from tqdm import tqdm
from llama_cpp import Llama

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def download_and_load_gguf_model(
    url: str,
    model_name: str,
    cache_dir: str = "local_models",
    n_ctx: int = 4096,
    n_threads: int = 8,
    n_gpu_layers: int = 0,
    verbose: bool = True
) -> Llama:
    """
    Downloads a GGUF model from a URL (if not already cached) and loads it with llama-cpp-python.

    Args:
        url (str): Direct URL to the .gguf model file.
        model_name (str): Filename to use for local caching (e.g. 'Hermes.gguf').
        cache_dir (str): Directory to store the client. Default is 'local_models'.
        n_ctx (int): Context window size.
        n_threads (int): CPU threads to use.
        n_gpu_layers (int): GPU layers to offload. Use 0 for CPU-only.
        verbose (bool): Print logs during loading.

    Returns:
        Llama: Loaded model ready for inference.
    """
    os.makedirs(cache_dir, exist_ok=True)
    model_path = os.path.join(cache_dir, model_name)

    if not os.path.exists(model_path):
        logger.info(f"Model not found locally. Downloading from:\n{url}")
        try:
            with requests.get(url, stream=True) as r:
                r.raise_for_status()
                total_size = int(r.headers.get("content-length", 0))
                with open(model_path, "wb") as f, tqdm(
                    total=total_size, unit='B', unit_scale=True, desc=model_name
                ) as bar:
                    for chunk in r.iter_content(chunk_size=8192):
                        f.write(chunk)
                        bar.update(len(chunk))
        except Exception as e:
            raise RuntimeError(f"Failed to download model: {e}")

    else:
        logger.info(f"Using cached model at: {model_path}")

    # Load with llama-cpp
    llm = Llama(
        model_path=model_path,
        n_ctx=n_ctx,
        n_threads=n_threads,
        n_gpu_layers=n_gpu_layers,
        verbose=verbose
    )

    logger.info("Model loaded successfully.")
    return llm

#%%
url = "https://huggingface.co/TheBloke/Hermes-2-Pro-Llama-3-GGUF/resolve/main/hermes-2-pro-llama-3.Q4_K_M.gguf"

model_name = "hermes-2-pro-llama-3.Q4_K_M.gguf"

llm = download_and_load_gguf_model(url, model_name)

prompt = "<|begin_of_text|><|start_header_id|>user<|end_header_id|>\nWhat is the capital of France?\n<|start_header_id|>assistant<|end_header_id|>\n"
response = llm(prompt=prompt, max_tokens=20, stop=["<|end_of_text|>"])
print(response["choices"][0]["text"].strip())

#%%
# Code to inference Hermes with HF Transformers
# Requires pytorch, transformers, bitsandbytes, sentencepiece, protobuf, and flash-attn packages

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, LlamaForCausalLM
import bitsandbytes, flash_attn

tokenizer = AutoTokenizer.from_pretrained('NousResearch/Hermes-3-Llama-3.1-8B', trust_remote_code=True)
client =  LlamaForCausalLM.from_pretrained(
    "NousResearch/Hermes-3-Llama-3.1-8B",
    torch_dtype=torch.float16,
    device_map="auto",
    load_in_8bit=False,
    load_in_4bit=True,
    use_flash_attention_2=True
)

prompts = [
    """<|im_start|>system
You are a sentient, superintelligent artificial general intelligence, here to teach and assist me.<|im_end|>
<|im_start|>user
Write a short story about Goku discovering kirby has teamed up with Majin Buu to destroy the world.<|im_end|>
<|im_start|>assistant""",
    ]

for chat in prompts:
    print(chat)
    input_ids = tokenizer(chat, return_tensors="pt").input_ids.to("cuda")
    generated_ids = client.generate(input_ids, max_new_tokens=750, temperature=0.8, repetition_penalty=1.1, do_sample=True, eos_token_id=tokenizer.eos_token_id)
    response = tokenizer.decode(generated_ids[0][input_ids.shape[-1]:], skip_special_tokens=True, clean_up_tokenization_space=True)
    print(f"Response: {response}")

#%%
url = "https://huggingface.co/TheBloke/Hermes-2-Pro-Llama-3-GGUF/resolve/main/hermes-2-pro-llama-3.Q4_K_M.gguf"
model_name = "hermes-2-pro-llama-3.Q4_K_M.gguf"

# Already avoids bitsandbytes
llm = download_and_load_gguf_model(url, model_name, n_gpu_layers=0)



from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "meta-llama/Llama-2-7b-hf"  # for example

client =  AutoModelForCausalLM.from_pretrained(model_name, device_map="auto")  # will crash without CUDA if quantized
