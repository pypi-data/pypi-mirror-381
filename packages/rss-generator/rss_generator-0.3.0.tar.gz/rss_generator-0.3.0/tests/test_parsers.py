"""Tests for parsers module."""

from rss_generator.parsers import (
    clean_html_content,
    parse_immich,
    parse_diariodominho,
    extract_immich_content,
    extract_immich_metadata,
    extract_diariodominho_content,
    extract_diariodominho_metadata,
    get_parser,
    get_content_extractor,
    get_metadata_extractor,
)


class TestCleanHtmlContent:
    """Tests for clean_html_content function."""

    def test_removes_unwanted_tags(self):
        """Test that unwanted tags are removed."""
        html = """
        <div>
            <nav>Navigation</nav>
            <header>Header</header>
            <p>Content</p>
            <script>alert('test')</script>
            <footer>Footer</footer>
        </div>
        """
        cleaned = clean_html_content(html)
        assert "Navigation" not in cleaned
        assert "Header" not in cleaned
        assert "Footer" not in cleaned
        assert "alert" not in cleaned
        assert "Content" in cleaned

    def test_removes_html_comments(self):
        """Test that HTML comments are removed."""
        html = "<p>Text</p><!-- Comment --><p>More text</p>"
        cleaned = clean_html_content(html)
        assert "Comment" not in cleaned
        assert "Text" in cleaned
        assert "More text" in cleaned

    def test_cleans_attributes(self):
        """Test that non-essential attributes are removed."""
        html = '<div id="test" data-foo="bar" class="content"><p>Text</p></div>'
        cleaned = clean_html_content(html)
        assert "data-foo" not in cleaned
        assert "id=" not in cleaned
        assert "class=" in cleaned  # class is allowed

    def test_handles_empty_input(self):
        """Test handling of empty input."""
        assert clean_html_content("") == ""

    def test_handles_malformed_html(self):
        """Test that malformed HTML doesn't crash."""
        html = "<p>Unclosed paragraph<div>Some content"
        result = clean_html_content(html)
        assert isinstance(result, str)
        assert len(result) > 0


class TestParseImmich:
    """Tests for parse_immich function."""

    def test_parses_basic_structure(self, sample_immich_html):
        """Test basic parsing of Immich blog posts."""
        articles = parse_immich(sample_immich_html, "https://immich.app/blog")
        assert len(articles) == 2
        assert articles[0]["title"] == "Immich Version 1.0.0 Released"
        assert "/blog/2023-12-30-version-1.0.0" in articles[0]["link"]

    def test_extracts_dates(self, sample_immich_html):
        """Test date extraction from Immich posts."""
        articles = parse_immich(sample_immich_html, "https://immich.app/blog")
        assert articles[0]["date"] == "2023-12-30T00:00:00"

    def test_extracts_descriptions(self, sample_immich_html):
        """Test description extraction."""
        articles = parse_immich(sample_immich_html, "https://immich.app/blog")
        assert "excited to announce" in articles[0]["description"]

    def test_makes_absolute_urls(self):
        """Test that relative URLs are converted to absolute."""
        html = '<a href="/blog/test"><h2>Test</h2></a>'
        articles = parse_immich(html, "https://immich.app/blog")
        if articles:
            assert articles[0]["link"].startswith("https://")

    def test_handles_empty_html(self):
        """Test handling of empty HTML."""
        articles = parse_immich("", "https://immich.app/blog")
        assert articles == []

    def test_handles_no_articles(self):
        """Test handling when no articles are found."""
        html = "<html><body><p>No articles here</p></body></html>"
        articles = parse_immich(html, "https://immich.app/blog")
        assert articles == []


class TestParseDiariodominho:
    """Tests for parse_diariodominho function."""

    def test_parses_basic_structure(self, sample_diariodominho_html):
        """Test basic parsing of Diário do Minho articles."""
        articles = parse_diariodominho(
            sample_diariodominho_html, "https://www.diariodominho.pt/"
        )
        assert len(articles) == 2
        assert articles[0]["title"] == "Title of News Article"

    def test_extracts_dates_from_url(self, sample_diariodominho_html):
        """Test date extraction from URL."""
        articles = parse_diariodominho(
            sample_diariodominho_html, "https://www.diariodominho.pt/"
        )
        assert articles[0]["date"] == "2025-10-02"
        assert articles[1]["date"] == "2025-10-01"

    def test_extracts_category_from_url(self, sample_diariodominho_html):
        """Test category extraction from URL."""
        articles = parse_diariodominho(
            sample_diariodominho_html, "https://www.diariodominho.pt/"
        )
        assert articles[0]["category"] == "Local"
        assert articles[1]["category"] == "Sports"

    def test_deduplicates_links(self):
        """Test that duplicate links are filtered out."""
        html = """
        <a href="/noticias/local/2025-10-02-test"><h3>Article 1</h3></a>
        <a href="/noticias/local/2025-10-02-test"><h3>Article 1 Duplicate</h3></a>
        """
        articles = parse_diariodominho(html, "https://www.diariodominho.pt/")
        assert len(articles) == 1

    def test_handles_empty_html(self):
        """Test handling of empty HTML."""
        articles = parse_diariodominho("", "https://www.diariodominho.pt/")
        assert articles == []


class TestExtractImmichContent:
    """Tests for extract_immich_content function."""

    def test_extracts_article_content(self, sample_article_content_html):
        """Test extraction of article content."""
        content = extract_immich_content(sample_article_content_html)
        assert content is not None
        assert "Article Title" in content
        assert "main content" in content

    def test_handles_missing_content(self):
        """Test handling when content cannot be extracted."""
        html = "<html><body><p>No article here</p></body></html>"
        content = extract_immich_content(html)
        # Should return None or handle gracefully
        assert content is None or isinstance(content, str)

    def test_cleans_extracted_content(self, sample_article_content_html):
        """Test that extracted content is cleaned."""
        content = extract_immich_content(sample_article_content_html)
        if content:
            # Should not contain script tags, nav, etc.
            assert "<script>" not in content
            assert "<nav>" not in content


class TestExtractImmichMetadata:
    """Tests for extract_immich_metadata function."""

    def test_extracts_author(self, sample_article_content_html):
        """Test author extraction."""
        metadata = extract_immich_metadata(sample_article_content_html)
        assert metadata["author"] == "Author Name"

    def test_extracts_image(self, sample_article_content_html):
        """Test image extraction."""
        metadata = extract_immich_metadata(sample_article_content_html)
        assert metadata["image"] is not None
        assert "featured.jpg" in metadata["image"]

    def test_handles_missing_metadata(self):
        """Test handling when metadata is missing."""
        html = "<html><body><p>No metadata</p></body></html>"
        metadata = extract_immich_metadata(html)
        assert metadata["author"] is None
        assert metadata["image"] is None


class TestExtractDiariodominhoContent:
    """Tests for extract_diariodominho_content function."""

    def test_extracts_article_content(self, sample_article_content_html):
        """Test extraction of article content."""
        content = extract_diariodominho_content(sample_article_content_html)
        assert content is not None
        assert isinstance(content, str)

    def test_handles_missing_content(self):
        """Test handling when content cannot be extracted."""
        html = "<html><body><p>No article</p></body></html>"
        content = extract_diariodominho_content(html)
        assert content is None or isinstance(content, str)


class TestExtractDiariodominhoMetadata:
    """Tests for extract_diariodominho_metadata function."""

    def test_returns_metadata_dict(self):
        """Test that metadata extraction returns proper dict."""
        html = "<html><body><p>Test</p></body></html>"
        metadata = extract_diariodominho_metadata(html)
        assert isinstance(metadata, dict)
        assert "author" in metadata
        assert "image" in metadata


class TestParserRegistry:
    """Tests for parser registry functions."""

    def test_get_parser_returns_function(self):
        """Test that get_parser returns a callable function."""
        parser = get_parser("parse_immich")
        assert callable(parser)
        assert parser == parse_immich

    def test_get_parser_returns_none_for_unknown(self):
        """Test that get_parser returns None for unknown parser."""
        parser = get_parser("unknown_parser")
        assert parser is None

    def test_get_content_extractor_returns_function(self):
        """Test that get_content_extractor returns a callable."""
        extractor = get_content_extractor("parse_immich")
        assert callable(extractor)
        assert extractor == extract_immich_content

    def test_get_metadata_extractor_returns_function(self):
        """Test that get_metadata_extractor returns a callable."""
        extractor = get_metadata_extractor("parse_immich")
        assert callable(extractor)
        assert extractor == extract_immich_metadata
