import os
from FlagEmbedding import FlagLLMReranker


def test_base_multi_devices():
    model = FlagLLMReranker(
        'BAAI/bge-reranker-v2-gemma',
        use_fp16=True,
        query_instruction_for_rerank="A: ",
        passage_instruction_for_rerank="B: ",
        devices=["cuda:3", "cuda:4"],   # if you don't have GPUs, you can use ["cpu", "cpu"]
        cache_dir=os.getenv('HF_HUB_CACHE', None),
    )
    
    pairs = [
        ["What is the capital of France?", "Paris is the capital of France."],
        ["What is the capital of France?", "The population of China is over 1.4 billion people."],
        ["What is the population of China?", "Paris is the capital of France."],
        ["What is the population of China?", "The population of China is over 1.4 billion people."]
    ] * 100
    
    scores = model.compute_score(pairs)
    
    print(scores[:4])


if __name__ == '__main__':
    test_base_multi_devices()
    
    print("--------------------------------")
    print("Expected Output:")
    print("[ 9.1484375  -4.50390625 -5.53125    10.21875   ]")
