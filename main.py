from manim import *

Text.set_default(font="Hiragino Mincho ProN")

class Opening(Scene):
    def construct(self):
        text = Paragraph("新入生の皆さん", "ご入学おめでとうございます！", alignment="center", line_spacing=1.5)

        self.play(Write(text))
        self.wait(10)
        self.play(FadeOut(text))


class AboutUs(Scene):
    def construct(self):
        nameText = Text("IT同好会", font_size=100)
        foundedText = Text("2025年1月設立", font_size=50)

        self.play(Write(nameText))

        nameText.generate_target()
        
        lines = VGroup(nameText.target, foundedText)
        lines.arrange(DOWN, buff=1)
        lines.move_to(ORIGIN)
        
        self.play(MoveToTarget(nameText), run_time=0.5)
        self.play(Write(foundedText))
        self.wait(2)
        self.play(FadeOut(foundedText))

        self.play(FadeOut(nameText[2:]), run_time=0.5)
        
        nameText_I = nameText[0]
        nameText_T = nameText[1]

        itText = Text("Information Technology", font_size=70)
        itTextJp = Text("情報技術", font_size=70)
        itTextJp.next_to(itText, DOWN)

        itText_I = itText[0]
        itText_T = itText[11]

        self.play(
            nameText_I.animate.move_to(itText_I.get_center()).scale(itText_I.height / nameText_I.height),
            nameText_T.animate.move_to(itText_T.get_center()).scale(itText_T.height / nameText_T.height),
        )

        self.play(Write(itText[1:11] + itText[12:]))
        self.wait(0.5)
        self.play(Write(itTextJp))
        self.wait(7)
        self.play(FadeOut(itText[1:11] + itText[12:]),
                  FadeOut(nameText_I),
                  FadeOut(nameText_T),
                  FadeOut(itTextJp),
                  run_time=1)
        

class AboutUs2(Scene):
    def construct(self):
        # タイトル
        title = Text("こんな人を待ってます", font_size=60, color=BLUE)
        title.to_edge(UP, buff=0.7)
        self.play(Write(title))

        bullet_points = [
            "・プログラミングやExcelに興味がある人",
            "・コンピュータについて幅広く学びたい人",
            "・さらにスキルアップを目指したい人"
        ]

        bullet_texts = VGroup(
            *[Text(item, font_size=36) for item in bullet_points]
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)

        bullet_texts.move_to(ORIGIN)
        for text in bullet_texts:
            self.play(FadeIn(text))
            self.wait(1)

        self.wait()

        self.play(FadeOut(bullet_texts), FadeOut(title))

        title = Text("活動について", font_size=60, color=BLUE)
        title.to_edge(UP, buff=0.7)
        self.play(Write(title))

        bullet_points = [
            "・オンラインでの情報共有や質問できる環境",
            "・自分の興味に合わせて学べる自由なスタイル",
            "・長期休みに講座を企画"
        ]

        bullet_texts = VGroup(
            *[Text(item, font_size=36) for item in bullet_points]
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)

        bullet_texts.move_to(ORIGIN)

        for text in bullet_texts:
            self.play(FadeIn(text))
            self.wait(3)
        
        self.wait(2)
        self.play(FadeOut(title), FadeOut(bullet_texts))
        


class FAQs(Scene):
    def construct(self):
        title = Text("よくある質問", font_size=48, color=BLUE)
        title.to_edge(UP, buff=0.7)
        self.play(Write(title))
        self.wait(2.5)

        faq_list = [
            ("初心者ですが、参加しても大丈夫ですか？", "やったことがない初心者でも全く問題ありません。\n「なんとなく興味がある」だけでも大歓迎です。\nやる気と興味があれば、どんなレベルからでも始められますし、\n興味がないのにやらないのは勿体無いです！"),
            ("どんなパソコンが必要ですか？", "WindowsでもMacでも大丈夫です。\nただしiPadなどのタブレットは非推奨とさせていただいております。"),
            ("活動は週にどれくらいありますか？", "オンラインでのやりとりはいつでも自由にできるスタイルです。\n活動は基本的に自由参加なので、\n忙しい時期や実習、アルバイトなどのスケジュールに合わせて\n無理なく続けられます。"),
            ("部費や費用はかかりますか？", "同好会としての部費はありません。\nただし、サービスによっては別途費用が発生することもありますので、\nその際は自己負担でお願いします。"),
            ("プログラミング以外のITスキルも学べますか？", "もちろんです！\nプログラムの自作以外にもExcelやWordなどのソフトの使い方\n多様なテーマで自由に交流しています。"),
            ("現在のメンバーは何人ですか？", "創設したばかりのため、現在のメンバーは2名（2年生と3年生）です。\nメンバーが増えてくれると嬉しいです！"),
            ("同好会とありますが、部活と異なる点はなんですか？","活動において同好会と部活の違いはありません。\n1年以上の活動と明確な活動実績によって部活に昇格することが出来ます。\n部活になると部室や部費を得ることができるようになるため、\n現在は部活になることを目標に活動しています。"),
        ]

        for question, answer in faq_list:
            question_text = Text(f"Q. {question}", font_size=36, color=YELLOW)
            question_text.next_to(title, DOWN, buff=0.8)

            answer_label = Text("A.", font_size=36)
            answer_paragraph = Paragraph(
                answer,
                font_size=30,
                alignment="LEFT",
                line_spacing=1.2
            )
 
            answer_label.next_to(answer_paragraph, LEFT, buff=0.3)
            answer_label.align_to(answer_paragraph, UP)

            answer_group = VGroup(answer_label, answer_paragraph)
            answer_group.next_to(question_text, DOWN, buff=0.7)
            faq_group = VGroup(question_text, answer_group)

            self.play(Write(question_text, run_time=1))
            self.wait(0.3)
            self.play(Create(answer_group), run_time=3)
            wait_time = len(answer) / 27
            self.wait(wait_time)

            self.play(FadeOut(faq_group))
            self.wait(0.5)

        self.play(FadeOut(title))

class Ending(Scene):
    def construct(self):
        # タイトル
        title = Text("IT同好会にぜひ！", font_size=48, color=BLUE)
        title.to_edge(UP, buff=0.7)

        # 要約されたメッセージ（1パラグラフ）
        paragraph = Paragraph(
            "ITスキルは将来にも役立つし、仲間と一緒に学べるのも魅力！",
            "少しでも気になったら、ぜひラウンジ新歓へ！",
            font_size=32,
            alignment="center",
            line_spacing=1.2,
        )
        text = Text("IT同好会一同、お待ちしてます！", font_size=32)
        paragraph.move_to(ORIGIN)
        text.next_to(paragraph, DOWN, buff=0.5)

        # アニメーション
        self.play(FadeIn(title))
        self.wait(0.5)

        self.play(Write(paragraph), run_time=4)
        self.wait(6.3)
        self.play(Write(text))
        self.wait(1.7)

        # フェードアウト
        self.play(FadeOut(title), FadeOut(paragraph), FadeOut(text))
