import os
import sys
from gift_blogger import generate_article_with_llm, generate_room_comment_with_llm

def test_main():
    print("Starting verification test for blogger-gift (LLM generation only)...")
    
    # GITHUB_TOKEN または GH_TOKEN が設定されているか確認（ない場合はPollinations AIがフォールバックとして使われます）
    github_token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if not github_token:
        print("Notice: GITHUB_TOKEN is not set. Will fallback to Pollinations AI (mistral/openai).")

    # ギフル向けのダミー商品データ（高級マカロン）
    dummy_item = {
        "itemName": "【ピエール・エルメ・パリ】極上マカロン 10個詰合わせ プレミアムスイーツギフト",
        "itemPrice": "4320",
        "itemUrl": "https://item.rakuten.co.jp/dummy/ph-macaron10/",
        "affiliateUrl": "https://hb.afl.rakuten.co.jp/hgc/dummy/?pc=https%3A%2F%2Fitem.rakuten.co.jp%2Fdummy%2Fph-macaron10%2F",
        "mediumImageUrls": [{"imageUrl": "https://thumbnail.image.rakuten.co.jp/@0_mall/dummy/cabinet/macaron10.jpg"}]
    }
        
    try:
        # LLMでBlogger記事生成
        print("Generating Blogger article with LLM...")
        content = generate_article_with_llm(dummy_item)
        
        print("\n=== GENERATED ARTICLE ===")
        print(content)
        print("==========================\n")

        # LLMで楽天ROOM用コメント生成
        print("Generating Rakuten Room comment with LLM...")
        room_comment = generate_room_comment_with_llm(dummy_item)
        print("\n=== GENERATED ROOM COMMENT ===")
        print(room_comment)
        print("==============================\n")
        
        print("Verification completed successfully!")

    except Exception as e:
        print(f"Error during verification: {e}")
        sys.exit(1)

if __name__ == "__main__":
    test_main()
