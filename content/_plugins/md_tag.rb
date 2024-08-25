module Jekyll
  class MarkdownBlock < Liquid::Block
    def initialize(tag_name, text, tokens)
      super
    end

    def render(context)
      # Get the content of the block and convert it to Markdown
      content = super.strip
      site = context.registers[:site]
      converter = site.find_converter_instance(Jekyll::Converters::Markdown)
      converter.convert(content)
    end
  end
end

Liquid::Template.register_tag('md', Jekyll::MarkdownBlock)
