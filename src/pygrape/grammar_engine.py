from pygrape import ualxiw_manager, LEXMASK_X_WEIGHTED_EXTRACTION_RTNO, \
    TO_FPRTN_AND_TOP_BLACKBOARD_EXTRACT_RTNO_PARSER, LRB_TREE, STD, string_to_u_array, u_array_to_string, \
    uaui_simple_segment_array_x_weight_array


class GrammarEngine:
    def __init__(self, grammar_pathname, bin_delaf_pathname):
        self.native_grammar_engine = ualxiw_manager(LEXMASK_X_WEIGHTED_EXTRACTION_RTNO, grammar_pathname,
                                                    bin_delaf_pathname)

    def reset_models(self, grammar_pathname, bin_delaf_pathname):
        self.native_grammar_engine = ualxiw_manager(LEXMASK_X_WEIGHTED_EXTRACTION_RTNO, grammar_pathname,
                                                    bin_delaf_pathname)

    def tag(self, sentence):
        native_sentence = string_to_u_array(sentence)
        self.native_grammar_engine.process(native_sentence.const_begin(), native_sentence.const_end(),
                                           TO_FPRTN_AND_TOP_BLACKBOARD_EXTRACT_RTNO_PARSER, True, False, LRB_TREE, STD)
        return self.native_grammar_engine.get_simplified_weighted_output()


    def movistarbot_translate(self, sentence):
        native_sentence = string_to_u_array(sentence)
        self.native_grammar_engine.process(native_sentence.const_begin(), native_sentence.const_end(),
                                           TO_FPRTN_AND_TOP_BLACKBOARD_EXTRACT_RTNO_PARSER, True, False, LRB_TREE, STD)
        native_result = self.native_grammar_engine.get_output_u_array()
        result = u_array_to_string(native_result)
        return result
