import textwrap

DEFAULT_WIDTH = 79
DEFAULT_SPACES_BEFORE = 0
DEFAULT_SPACES_AFTER = 1

class Commenter:
    def __init__(self, start='', end='', multiline=None, multiline_header=None, multiline_alignto=True,
                       multiline_start_newline=False, spaces_before=DEFAULT_SPACES_BEFORE,
                       spaces_after=DEFAULT_SPACES_AFTER, multiline_spaces_after=None, multiline_start=None,
                       multiline_end=None, width=DEFAULT_WIDTH):
        self.width = width
        self.start = start
        self.end = end
        self.spaces_before = int(spaces_before)
        self.spaces_after = int(spaces_after)
        self.multiline_spaces_after = int(multiline_spaces_after) if multiline_spaces_after is not None else None

        self.multiline = bool(multiline) if multiline is not None else True if multiline_start is not None and multiline_end is not None else False
        self.multiline_header = multiline_header if multiline_header is not None else ''
        self.multiline_start = multiline_start if multiline_start is not None else self.start
        self.multiline_end = multiline_end if multiline_start is not None else self.end
        self.multiline_alignto = multiline_alignto
        self.multiline_start_newline = bool(multiline_start_newline)

        self.check_width(*self.calc_spacing())

    def calc_spacing(self, multiline=None, multiline_alignto=None, multiline_start_newline=None, spaces_before=None,
                       spaces_after=None, multiline_spaces_after=None):

        spaces_before = int(spaces_before) if spaces_before is not None else self.spaces_before
        spaces_after = int(spaces_after) if spaces_after is not None else self.spaces_after
        multiline_spaces_after = int(multiline_spaces_after) if multiline_spaces_after else self.multiline_spaces_after if self.multiline_spaces_after is not None else spaces_after
        multiline_alignto = multiline_alignto if multiline_alignto is not None else self.multiline_alignto

        start_pre_spacing = spaces_before
        start_post_spacing = spaces_after
        end_pre_spacing = spaces_before
        multiline_pre_spacing = spaces_before
        multiline_post_spacing = multiline_spaces_after
        single_line_pre_spacing = spaces_before
        single_line_inner_spacing = spaces_after

        if multiline and multiline_alignto is not False:
            align_str = ''
            if isinstance(multiline_alignto, str) and len(multiline_alignto) > 0:
                align_str = multiline_alignto
                if align_str not in self.start or align_str not in self.end:
                    raise ValueError("multiline_alignto '{}' does not existing in both '{}' and '{}'".format(multiline_alignto, self.start, self.end))
            elif multiline_alignto is True:
                if len(self.multiline_header) > 0 and (self.multiline_header in self.multiline_start and self.multiline_header in self.multiline_end):
                    align_str = self.multiline_header
                elif len(self.multiline_header) == 0:
                    for i in range(len(self.multiline_end)):
                        for j in range(i+1, len(self.multiline_end)+1):
                            align_candidate_str = self.multiline_end[i:j]
                            if align_candidate_str in self.multiline_start and len(align_candidate_str) > len(align_str):
                                align_str = align_candidate_str
            else:
                raise ValueError("Invalid multiline_alignto '{}'".format(multiline_alignto))

            if len(align_str) > 0:
                align_start_offset = self.multiline_start.find(align_str)
                align_end_offset = self.multiline_end.find(align_str)
            else:
                align_start_offset = start_pre_spacing + len(self.multiline_start)
                align_end_offset = end_pre_spacing + len(self.multiline_end)

            start_pre_spacing += max(align_end_offset - align_start_offset, 0)
            end_pre_spacing += max(align_start_offset - align_end_offset, 0)

            multiline_pre_spacing += max(max(align_end_offset, align_start_offset) + len(align_str) - len(self.multiline_header), 0)
            start_len = start_pre_spacing + len(self.multiline_start) + start_post_spacing
            multi_len = multiline_pre_spacing + len(self.multiline_header) + multiline_post_spacing
            start_post_spacing += max(multi_len - start_len, 0)
            multiline_post_spacing += max(start_len - multi_len, 0)

        return start_pre_spacing, start_post_spacing, end_pre_spacing, multiline_pre_spacing, multiline_post_spacing, single_line_pre_spacing, single_line_inner_spacing

    def single_comment_len(self, single_line_pre_spacing, single_line_inner_spacing):
        return len(self.single_line_start(single_line_pre_spacing, single_line_inner_spacing)) + len(self.single_line_end(single_line_inner_spacing))

    def multi_comment_len(self, start_pre_spacing, start_post_spacing, end_pre_spacing, multiline_pre_spacing, multiline_post_spacing, multiline_start_newline):
        return max(len(self.multi_line_start(start_pre_spacing, start_post_spacing, multiline_post_spacing, multiline_start_newline).split('\n')[0]),
                   len(self.multi_line_mid(multiline_pre_spacing, multiline_post_spacing)),
                   len(self.multi_line_end(end_pre_spacing)))

    def single_line_start(self, single_line_pre_spacing, single_line_inner_spacing):
        return ' ' * single_line_pre_spacing + self.start + ' ' * single_line_inner_spacing

    def single_line_end(self, single_line_inner_spacing):
        return ' ' * single_line_inner_spacing + self.end if len(self.end) > 0 else ''

    def multi_line_start(self, start_pre_spacing, start_post_spacing, multiline_post_spacing, multiline_start_newline):
        return ' ' * start_pre_spacing + self.multiline_start + (' ' * start_post_spacing if multiline_start_newline is not True else '')

    def multi_line_mid(self, multiline_pre_spacing, multiline_post_spacing):
        return ' ' * multiline_pre_spacing + self.multiline_header + ' ' * multiline_post_spacing

    def multi_line_end(self, end_pre_spacing):
        return ' ' * end_pre_spacing + self.multiline_end

    def check_width(self, start_pre_spacing, start_post_spacing, end_pre_spacing, multiline_pre_spacing,
                          multiline_post_spacing, single_line_pre_spacing, single_line_inner_spacing,
                          *, width=None, multiline=None, multiline_start_newline=None):
        width = int(width) if width is not None else self.width
        multiline = bool(multiline) if multiline is not None and self.multiline is True else self.multiline
        multiline_start_newline = bool(multiline_start_newline) if multiline_start_newline is not None else self.multiline_start_newline

        if width <= self.single_comment_len(single_line_pre_spacing, single_line_inner_spacing):
            raise ValueError("Width of '{}' is too small for opening '{}' and ending '{}'".format(width,
                       self.single_line_start(single_line_pre_spacing, single_line_inner_spacing),
                       self.single_line_end(single_line_inner_spacing)))
        if multiline and width <= self.multi_comment_len(start_pre_spacing, start_post_spacing,
                                                         end_pre_spacing, multiline_pre_spacing,
                                                         multiline_post_spacing, multiline_start_newline):
            raise ValueError("Width of '{}' is too small for opening '{}', mid header '{}', and ending '{}'".format(width,
                            self.multi_line_start(start_pre_spacing, start_post_spacing, multiline_post_spacing, multiline_start_newline),
                            self.multi_line_mid(multiline_pre_spacing, multiline_post_spacing),
                            self.multi_line_end(end_pre_spacing)))

    def __str__(self):
        start_pre_spacing, \
        start_post_spacing, \
        end_pre_spacing, \
        multiline_pre_spacing, \
        multiline_post_spacing, \
        single_line_pre_spacing, \
        single_line_inner_spacing = self.calc_spacing()

        single_line_start = self.single_line_start(single_line_pre_spacing, single_line_inner_spacing)
        single_line_end = self.single_line_end(single_line_inner_spacing)
        multi_line_start = self.multi_line_start(start_pre_spacing, start_post_spacing, multiline_post_spacing, self.multiline_start_newline)
        multi_line_end = self.multi_line_end(end_pre_spacing)

        ret_str = "Comment in the form '{} ... {}'".format(single_line_start, single_line_end)
        if self.multiline and (single_line_start != multi_line_start or single_line_end != multi_line_end):
            ret_str += " or '{} ... {}' in the multiline case".format(multi_line_start, multi_line_end)
        if len(self.multiline_header) > 0:
            ret_str += " with {} as the header for each line".format(self.multi_line_mid(multiline_pre_spacing, multiline_post_spacing))
        return ret_str

    def __call__(self, text, width=None, multiline=None, multiline_header=None, multiline_alignto=None,
            multiline_start_newline=None, spaces_before=None, spaces_after=None, multiline_spaces_after=None):

        def single_line_str(text, single_line_pre_spacing, single_line_inner_spacing):
            return self.single_line_start(single_line_pre_spacing,
                                          single_line_inner_spacing) + text + self.single_line_end(single_line_inner_spacing)

        def multi_line_start_str(text, start_pre_spacing, start_post_spacing, multiline_post_spacing, multiline_start_newline):
            return self.multi_line_start(start_pre_spacing, start_post_spacing, multiline_post_spacing, multiline_start_newline) + (text if multiline_start_newline is False else '')

        def multi_line_mid_str(text, multiline_pre_spacing, multiline_post_spacing):
            return '\n' + self.multi_line_mid(multiline_pre_spacing, multiline_post_spacing) + text

        def multi_line_end_str(end_pre_spacing):
            return '\n' + self.multi_line_end(end_pre_spacing)

        width = int(width) if width is not None else self.width
        multiline = bool(multiline) if multiline is not None and self.multiline is True else self.multiline
        multiline_start_newline = bool(multiline_start_newline) if multiline_start_newline is not None else self.multiline_start_newline

        start_pre_spacing, \
        start_post_spacing, \
        end_pre_spacing, \
        multiline_pre_spacing, \
        multiline_post_spacing, \
        single_line_pre_spacing, \
        single_line_inner_spacing = self.calc_spacing(spaces_before=spaces_before,
                                                      spaces_after=spaces_after,
                                                      multiline=multiline,
                                                      multiline_spaces_after=multiline_spaces_after,
                                                      multiline_start_newline=multiline_start_newline,
                                                      multiline_alignto=multiline_alignto)

        self.check_width(start_pre_spacing, start_post_spacing, end_pre_spacing, multiline_pre_spacing,
                        multiline_post_spacing, single_line_pre_spacing, single_line_inner_spacing,
                        width=width, multiline=multiline, multiline_start_newline=multiline_start_newline)

        single_comment_len = self.single_comment_len(single_line_pre_spacing, single_line_inner_spacing)
        text = text.split('\n')
        if len(text) == 1 and len(text[0]) + single_comment_len <= width:
            return single_line_str(text[0], single_line_pre_spacing, single_line_inner_spacing)
        text_len = width - single_comment_len
        if multiline:
            text_len = width - self.multi_comment_len(start_pre_spacing, start_post_spacing, end_pre_spacing,
                                                      multiline_pre_spacing, multiline_post_spacing, multiline_start_newline)
        text_lines = []
        for text_line in text:
            text_lines.extend(textwrap.wrap(text_line, width=text_len))
        if multiline:
            mid_text = text_lines[1:] if multiline_start_newline is False else text
            return multi_line_start_str(text_lines[0], start_pre_spacing, start_post_spacing, multiline_post_spacing, multiline_start_newline) \
                    + ''.join([multi_line_mid_str(x, multiline_pre_spacing, multiline_post_spacing) for x in mid_text]) \
                    + multi_line_end_str(end_pre_spacing) + '\n'
        else:
            return '\n'.join([single_line_str(x, single_line_pre_spacing, single_line_inner_spacing) for x in text_lines])

