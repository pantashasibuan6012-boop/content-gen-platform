#!/usr/bin/env python3
"""Content Generation Platform."""

import json, sys
from dataclasses import dataclass, field

@dataclass
class ContentRequest:
    topic: str
    content_type: str = "blog"
    language: str = "en"
    tone: str = "professional"
    word_count: int = 500

@dataclass
class GeneratedContent:
    request: ContentRequest
    title: str = ""
    body: str = ""
    seo_score: float = 0.0
    variants: list = field(default_factory=list)

class ContentGenerator:
    TONES = {"professional", "casual", "friendly", "formal", "humorous"}
    TYPES = {"blog", "social", "email", "ad", "description"}

    def generate(self, req: ContentRequest) -> GeneratedContent:
        result = GeneratedContent(request=req)
        result.title = self._gen_title(req)
        result.body = self._gen_body(req)
        result.seo_score = self._calc_seo(result)
        return result

    def _gen_title(self, req: ContentRequest) -> str:
        titles = {
            "blog": f"The Ultimate Guide to {req.topic.title()}",
            "social": f"Discover {req.topic.title()} - Here's What You Need to Know",
            "email": f"Your {req.topic.title()} Update",
            "ad": f"Transform Your {req.topic.title()} Today",
        }
        return titles.get(req.content_type, f"About {req.topic.title()}")

    def _gen_body(self, req: ContentRequest) -> str:
        return f"""This is a comprehensive {req.content_type} about {req.topic}.

Key Points:
1. Understanding {req.topic} fundamentals
2. Best practices and implementation strategies
3. Real-world case studies and examples
4. Future trends and predictions

The {req.topic} landscape is rapidly evolving. Organizations that adapt early gain significant competitive advantages. Our research shows that implementing these strategies can improve outcomes by 40%.

Conclusion: {req.topic.title()} represents a major opportunity for growth and innovation."""

    def _calc_seo(self, content: GeneratedContent) -> float:
        score = 0.5
        if len(content.title) > 10:
            score += 0.1
        if len(content.body) > 200:
            score += 0.2
        if content.request.topic.lower() in content.body.lower():
            score += 0.2
        return min(1.0, score)

    def batch_generate(self, requests: list) -> list:
        return [self.gen(r) for r in requests]

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py generate --topic 'AI' --type blog")
        sys.exit(1)
    gen = ContentGenerator()
    topic = "AI trends"
    if "--topic" in sys.argv:
        topic = sys.argv[sys.argv.index("--topic") + 1]
    req = ContentRequest(topic=topic)
    result = gen.generate(req)
    print(f"Title: {result.title}")
    print(f"SEO Score: {result.seo_score:.0%}")
    print(f"\n{result.body}")

if __name__ == "__main__":
    main()
