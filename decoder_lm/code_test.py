import os
import numpy as np
from models import load_text_generation_model
from tensor_flops import compute_tensor_flops, compute_forward_flops


os.environ["TOKENIZERS_PARALLELISM"] = "true"

model_name = "facebook/opt-125m"

model = load_text_generation_model(
    model_name, "lora",
    output_attentions=False,
)

# t_dy, t_dw = compute_tensor_flops(
#     model=model,
#     model_name=model_name,
#     input_length=1024,
#     batch_size=4,
#     draw_figure=True,
# )

# t_forward = compute_forward_flops(
#     model=model,
#     model_name=model_name,
#     input_length=1024,
#     batch_size=4,
# )

# print(f"bp/fp = {np.sum(t_dy + t_dw) / t_forward}")


# summary = layer_summary(model, print_summary=True)
# compute_tensor_flops(summary, num_tokens=512, batch_size=4, draw_figure=True)
    
# ._parameters, in_features, out_features

for k, (name, param) in enumerate(model.named_parameters()):
    if param.requires_grad:
        print(k, name)


# train_loader, tokenizer = load_samsum_for_t5small(
#     split="train", 
#     max_input_length=512, 
#     max_output_length=256,
#     batch_size=8,
#     shuffle=True,
#     keep_in_memory=True,
#     print_info=False,
# )

# print(model)

# # profile_batch_time(
# #     model=model,
# #     dataloader=train_loader,
# # )

# profile_training(
#     model=model,
#     dataloader=train_loader,
#     folder_name="t5small_samsum",
# )

"""
0 transformer.word_embeddings.weight torch.Size([250880, 1024])
1 transformer.word_embeddings_layernorm.weight torch.Size([1024])
2 transformer.word_embeddings_layernorm.bias torch.Size([1024])
3 transformer.h.0.input_layernorm.weight torch.Size([1024])
4 transformer.h.0.input_layernorm.bias torch.Size([1024])
5 transformer.h.0.self_attention.query_key_value.weight torch.Size([3072, 1024])
6 transformer.h.0.self_attention.query_key_value.bias torch.Size([3072])
7 transformer.h.0.self_attention.dense.weight torch.Size([1024, 1024])
8 transformer.h.0.self_attention.dense.bias torch.Size([1024])
9 transformer.h.0.post_attention_layernorm.weight torch.Size([1024])
10 transformer.h.0.post_attention_layernorm.bias torch.Size([1024])
11 transformer.h.0.mlp.dense_h_to_4h.weight torch.Size([4096, 1024])
12 transformer.h.0.mlp.dense_h_to_4h.bias torch.Size([4096])
13 transformer.h.0.mlp.dense_4h_to_h.weight torch.Size([1024, 4096])
14 transformer.h.0.mlp.dense_4h_to_h.bias torch.Size([1024])
15 transformer.h.1.input_layernorm.weight torch.Size([1024])
16 transformer.h.1.input_layernorm.bias torch.Size([1024])
17 transformer.h.1.self_attention.query_key_value.weight torch.Size([3072, 1024])
18 transformer.h.1.self_attention.query_key_value.bias torch.Size([3072])
19 transformer.h.1.self_attention.dense.weight torch.Size([1024, 1024])
20 transformer.h.1.self_attention.dense.bias torch.Size([1024])
21 transformer.h.1.post_attention_layernorm.weight torch.Size([1024])
22 transformer.h.1.post_attention_layernorm.bias torch.Size([1024])
23 transformer.h.1.mlp.dense_h_to_4h.weight torch.Size([4096, 1024])
24 transformer.h.1.mlp.dense_h_to_4h.bias torch.Size([4096])
25 transformer.h.1.mlp.dense_4h_to_h.weight torch.Size([1024, 4096])
26 transformer.h.1.mlp.dense_4h_to_h.bias torch.Size([1024])
27 transformer.h.2.input_layernorm.weight torch.Size([1024])
28 transformer.h.2.input_layernorm.bias torch.Size([1024])
29 transformer.h.2.self_attention.query_key_value.weight torch.Size([3072, 1024])
30 transformer.h.2.self_attention.query_key_value.bias torch.Size([3072])
31 transformer.h.2.self_attention.dense.weight torch.Size([1024, 1024])
32 transformer.h.2.self_attention.dense.bias torch.Size([1024])
33 transformer.h.2.post_attention_layernorm.weight torch.Size([1024])
34 transformer.h.2.post_attention_layernorm.bias torch.Size([1024])
35 transformer.h.2.mlp.dense_h_to_4h.weight torch.Size([4096, 1024])
36 transformer.h.2.mlp.dense_h_to_4h.bias torch.Size([4096])
37 transformer.h.2.mlp.dense_4h_to_h.weight torch.Size([1024, 4096])
38 transformer.h.2.mlp.dense_4h_to_h.bias torch.Size([1024])
39 transformer.h.3.input_layernorm.weight torch.Size([1024])
40 transformer.h.3.input_layernorm.bias torch.Size([1024])
41 transformer.h.3.self_attention.query_key_value.weight torch.Size([3072, 1024])
42 transformer.h.3.self_attention.query_key_value.bias torch.Size([3072])
43 transformer.h.3.self_attention.dense.weight torch.Size([1024, 1024])
44 transformer.h.3.self_attention.dense.bias torch.Size([1024])
45 transformer.h.3.post_attention_layernorm.weight torch.Size([1024])
46 transformer.h.3.post_attention_layernorm.bias torch.Size([1024])
47 transformer.h.3.mlp.dense_h_to_4h.weight torch.Size([4096, 1024])
48 transformer.h.3.mlp.dense_h_to_4h.bias torch.Size([4096])
49 transformer.h.3.mlp.dense_4h_to_h.weight torch.Size([1024, 4096])
50 transformer.h.3.mlp.dense_4h_to_h.bias torch.Size([1024])
51 transformer.h.4.input_layernorm.weight torch.Size([1024])
52 transformer.h.4.input_layernorm.bias torch.Size([1024])
53 transformer.h.4.self_attention.query_key_value.weight torch.Size([3072, 1024])
54 transformer.h.4.self_attention.query_key_value.bias torch.Size([3072])
55 transformer.h.4.self_attention.dense.weight torch.Size([1024, 1024])
56 transformer.h.4.self_attention.dense.bias torch.Size([1024])
57 transformer.h.4.post_attention_layernorm.weight torch.Size([1024])
58 transformer.h.4.post_attention_layernorm.bias torch.Size([1024])
59 transformer.h.4.mlp.dense_h_to_4h.weight torch.Size([4096, 1024])
60 transformer.h.4.mlp.dense_h_to_4h.bias torch.Size([4096])
61 transformer.h.4.mlp.dense_4h_to_h.weight torch.Size([1024, 4096])
62 transformer.h.4.mlp.dense_4h_to_h.bias torch.Size([1024])
63 transformer.h.5.input_layernorm.weight torch.Size([1024])
64 transformer.h.5.input_layernorm.bias torch.Size([1024])
65 transformer.h.5.self_attention.query_key_value.weight torch.Size([3072, 1024])
66 transformer.h.5.self_attention.query_key_value.bias torch.Size([3072])
67 transformer.h.5.self_attention.dense.weight torch.Size([1024, 1024])
68 transformer.h.5.self_attention.dense.bias torch.Size([1024])
69 transformer.h.5.post_attention_layernorm.weight torch.Size([1024])
70 transformer.h.5.post_attention_layernorm.bias torch.Size([1024])
71 transformer.h.5.mlp.dense_h_to_4h.weight torch.Size([4096, 1024])
72 transformer.h.5.mlp.dense_h_to_4h.bias torch.Size([4096])
73 transformer.h.5.mlp.dense_4h_to_h.weight torch.Size([1024, 4096])
74 transformer.h.5.mlp.dense_4h_to_h.bias torch.Size([1024])
75 transformer.h.6.input_layernorm.weight torch.Size([1024])
76 transformer.h.6.input_layernorm.bias torch.Size([1024])
77 transformer.h.6.self_attention.query_key_value.weight torch.Size([3072, 1024])
78 transformer.h.6.self_attention.query_key_value.bias torch.Size([3072])
79 transformer.h.6.self_attention.dense.weight torch.Size([1024, 1024])
80 transformer.h.6.self_attention.dense.bias torch.Size([1024])
81 transformer.h.6.post_attention_layernorm.weight torch.Size([1024])
82 transformer.h.6.post_attention_layernorm.bias torch.Size([1024])
83 transformer.h.6.mlp.dense_h_to_4h.weight torch.Size([4096, 1024])
84 transformer.h.6.mlp.dense_h_to_4h.bias torch.Size([4096])
85 transformer.h.6.mlp.dense_4h_to_h.weight torch.Size([1024, 4096])
86 transformer.h.6.mlp.dense_4h_to_h.bias torch.Size([1024])
87 transformer.h.7.input_layernorm.weight torch.Size([1024])
88 transformer.h.7.input_layernorm.bias torch.Size([1024])
89 transformer.h.7.self_attention.query_key_value.weight torch.Size([3072, 1024])
90 transformer.h.7.self_attention.query_key_value.bias torch.Size([3072])
91 transformer.h.7.self_attention.dense.weight torch.Size([1024, 1024])
92 transformer.h.7.self_attention.dense.bias torch.Size([1024])
93 transformer.h.7.post_attention_layernorm.weight torch.Size([1024])
94 transformer.h.7.post_attention_layernorm.bias torch.Size([1024])
95 transformer.h.7.mlp.dense_h_to_4h.weight torch.Size([4096, 1024])
96 transformer.h.7.mlp.dense_h_to_4h.bias torch.Size([4096])
97 transformer.h.7.mlp.dense_4h_to_h.weight torch.Size([1024, 4096])
98 transformer.h.7.mlp.dense_4h_to_h.bias torch.Size([1024])
99 transformer.h.8.input_layernorm.weight torch.Size([1024])
100 transformer.h.8.input_layernorm.bias torch.Size([1024])
101 transformer.h.8.self_attention.query_key_value.weight torch.Size([3072, 1024])
102 transformer.h.8.self_attention.query_key_value.bias torch.Size([3072])
103 transformer.h.8.self_attention.dense.weight torch.Size([1024, 1024])
104 transformer.h.8.self_attention.dense.bias torch.Size([1024])
105 transformer.h.8.post_attention_layernorm.weight torch.Size([1024])
106 transformer.h.8.post_attention_layernorm.bias torch.Size([1024])
107 transformer.h.8.mlp.dense_h_to_4h.weight torch.Size([4096, 1024])
108 transformer.h.8.mlp.dense_h_to_4h.bias torch.Size([4096])
109 transformer.h.8.mlp.dense_4h_to_h.weight torch.Size([1024, 4096])
110 transformer.h.8.mlp.dense_4h_to_h.bias torch.Size([1024])
111 transformer.h.9.input_layernorm.weight torch.Size([1024])
112 transformer.h.9.input_layernorm.bias torch.Size([1024])
113 transformer.h.9.self_attention.query_key_value.weight torch.Size([3072, 1024])
114 transformer.h.9.self_attention.query_key_value.bias torch.Size([3072])
115 transformer.h.9.self_attention.dense.weight torch.Size([1024, 1024])
116 transformer.h.9.self_attention.dense.bias torch.Size([1024])
117 transformer.h.9.post_attention_layernorm.weight torch.Size([1024])
118 transformer.h.9.post_attention_layernorm.bias torch.Size([1024])
119 transformer.h.9.mlp.dense_h_to_4h.weight torch.Size([4096, 1024])
120 transformer.h.9.mlp.dense_h_to_4h.bias torch.Size([4096])
121 transformer.h.9.mlp.dense_4h_to_h.weight torch.Size([1024, 4096])
122 transformer.h.9.mlp.dense_4h_to_h.bias torch.Size([1024])
123 transformer.h.10.input_layernorm.weight torch.Size([1024])
124 transformer.h.10.input_layernorm.bias torch.Size([1024])
125 transformer.h.10.self_attention.query_key_value.weight torch.Size([3072, 1024])
126 transformer.h.10.self_attention.query_key_value.bias torch.Size([3072])
127 transformer.h.10.self_attention.dense.weight torch.Size([1024, 1024])
128 transformer.h.10.self_attention.dense.bias torch.Size([1024])
129 transformer.h.10.post_attention_layernorm.weight torch.Size([1024])
130 transformer.h.10.post_attention_layernorm.bias torch.Size([1024])
131 transformer.h.10.mlp.dense_h_to_4h.weight torch.Size([4096, 1024])
132 transformer.h.10.mlp.dense_h_to_4h.bias torch.Size([4096])
133 transformer.h.10.mlp.dense_4h_to_h.weight torch.Size([1024, 4096])
134 transformer.h.10.mlp.dense_4h_to_h.bias torch.Size([1024])
135 transformer.h.11.input_layernorm.weight torch.Size([1024])
136 transformer.h.11.input_layernorm.bias torch.Size([1024])
137 transformer.h.11.self_attention.query_key_value.weight torch.Size([3072, 1024])
138 transformer.h.11.self_attention.query_key_value.bias torch.Size([3072])
139 transformer.h.11.self_attention.dense.weight torch.Size([1024, 1024])
140 transformer.h.11.self_attention.dense.bias torch.Size([1024])
141 transformer.h.11.post_attention_layernorm.weight torch.Size([1024])
142 transformer.h.11.post_attention_layernorm.bias torch.Size([1024])
143 transformer.h.11.mlp.dense_h_to_4h.weight torch.Size([4096, 1024])
144 transformer.h.11.mlp.dense_h_to_4h.bias torch.Size([4096])
145 transformer.h.11.mlp.dense_4h_to_h.weight torch.Size([1024, 4096])
146 transformer.h.11.mlp.dense_4h_to_h.bias torch.Size([1024])
147 transformer.h.12.input_layernorm.weight torch.Size([1024])
148 transformer.h.12.input_layernorm.bias torch.Size([1024])
149 transformer.h.12.self_attention.query_key_value.weight torch.Size([3072, 1024])
150 transformer.h.12.self_attention.query_key_value.bias torch.Size([3072])
151 transformer.h.12.self_attention.dense.weight torch.Size([1024, 1024])
152 transformer.h.12.self_attention.dense.bias torch.Size([1024])
153 transformer.h.12.post_attention_layernorm.weight torch.Size([1024])
154 transformer.h.12.post_attention_layernorm.bias torch.Size([1024])
155 transformer.h.12.mlp.dense_h_to_4h.weight torch.Size([4096, 1024])
156 transformer.h.12.mlp.dense_h_to_4h.bias torch.Size([4096])
157 transformer.h.12.mlp.dense_4h_to_h.weight torch.Size([1024, 4096])
158 transformer.h.12.mlp.dense_4h_to_h.bias torch.Size([1024])
159 transformer.h.13.input_layernorm.weight torch.Size([1024])
160 transformer.h.13.input_layernorm.bias torch.Size([1024])
161 transformer.h.13.self_attention.query_key_value.weight torch.Size([3072, 1024])
162 transformer.h.13.self_attention.query_key_value.bias torch.Size([3072])
163 transformer.h.13.self_attention.dense.weight torch.Size([1024, 1024])
164 transformer.h.13.self_attention.dense.bias torch.Size([1024])
165 transformer.h.13.post_attention_layernorm.weight torch.Size([1024])
166 transformer.h.13.post_attention_layernorm.bias torch.Size([1024])
167 transformer.h.13.mlp.dense_h_to_4h.weight torch.Size([4096, 1024])
168 transformer.h.13.mlp.dense_h_to_4h.bias torch.Size([4096])
169 transformer.h.13.mlp.dense_4h_to_h.weight torch.Size([1024, 4096])
170 transformer.h.13.mlp.dense_4h_to_h.bias torch.Size([1024])
171 transformer.h.14.input_layernorm.weight torch.Size([1024])
172 transformer.h.14.input_layernorm.bias torch.Size([1024])
173 transformer.h.14.self_attention.query_key_value.weight torch.Size([3072, 1024])
174 transformer.h.14.self_attention.query_key_value.bias torch.Size([3072])
175 transformer.h.14.self_attention.dense.weight torch.Size([1024, 1024])
176 transformer.h.14.self_attention.dense.bias torch.Size([1024])
177 transformer.h.14.post_attention_layernorm.weight torch.Size([1024])
178 transformer.h.14.post_attention_layernorm.bias torch.Size([1024])
179 transformer.h.14.mlp.dense_h_to_4h.weight torch.Size([4096, 1024])
180 transformer.h.14.mlp.dense_h_to_4h.bias torch.Size([4096])
181 transformer.h.14.mlp.dense_4h_to_h.weight torch.Size([1024, 4096])
182 transformer.h.14.mlp.dense_4h_to_h.bias torch.Size([1024])
183 transformer.h.15.input_layernorm.weight torch.Size([1024])
184 transformer.h.15.input_layernorm.bias torch.Size([1024])
185 transformer.h.15.self_attention.query_key_value.weight torch.Size([3072, 1024])
186 transformer.h.15.self_attention.query_key_value.bias torch.Size([3072])
187 transformer.h.15.self_attention.dense.weight torch.Size([1024, 1024])
188 transformer.h.15.self_attention.dense.bias torch.Size([1024])
189 transformer.h.15.post_attention_layernorm.weight torch.Size([1024])
190 transformer.h.15.post_attention_layernorm.bias torch.Size([1024])
191 transformer.h.15.mlp.dense_h_to_4h.weight torch.Size([4096, 1024])
192 transformer.h.15.mlp.dense_h_to_4h.bias torch.Size([4096])
193 transformer.h.15.mlp.dense_4h_to_h.weight torch.Size([1024, 4096])
194 transformer.h.15.mlp.dense_4h_to_h.bias torch.Size([1024])
195 transformer.h.16.input_layernorm.weight torch.Size([1024])
196 transformer.h.16.input_layernorm.bias torch.Size([1024])
197 transformer.h.16.self_attention.query_key_value.weight torch.Size([3072, 1024])
198 transformer.h.16.self_attention.query_key_value.bias torch.Size([3072])
199 transformer.h.16.self_attention.dense.weight torch.Size([1024, 1024])
200 transformer.h.16.self_attention.dense.bias torch.Size([1024])
201 transformer.h.16.post_attention_layernorm.weight torch.Size([1024])
202 transformer.h.16.post_attention_layernorm.bias torch.Size([1024])
203 transformer.h.16.mlp.dense_h_to_4h.weight torch.Size([4096, 1024])
204 transformer.h.16.mlp.dense_h_to_4h.bias torch.Size([4096])
205 transformer.h.16.mlp.dense_4h_to_h.weight torch.Size([1024, 4096])
206 transformer.h.16.mlp.dense_4h_to_h.bias torch.Size([1024])
207 transformer.h.17.input_layernorm.weight torch.Size([1024])
208 transformer.h.17.input_layernorm.bias torch.Size([1024])
209 transformer.h.17.self_attention.query_key_value.weight torch.Size([3072, 1024])
210 transformer.h.17.self_attention.query_key_value.bias torch.Size([3072])
211 transformer.h.17.self_attention.dense.weight torch.Size([1024, 1024])
212 transformer.h.17.self_attention.dense.bias torch.Size([1024])
213 transformer.h.17.post_attention_layernorm.weight torch.Size([1024])
214 transformer.h.17.post_attention_layernorm.bias torch.Size([1024])
215 transformer.h.17.mlp.dense_h_to_4h.weight torch.Size([4096, 1024])
216 transformer.h.17.mlp.dense_h_to_4h.bias torch.Size([4096])
217 transformer.h.17.mlp.dense_4h_to_h.weight torch.Size([1024, 4096])
218 transformer.h.17.mlp.dense_4h_to_h.bias torch.Size([1024])
219 transformer.h.18.input_layernorm.weight torch.Size([1024])
220 transformer.h.18.input_layernorm.bias torch.Size([1024])
221 transformer.h.18.self_attention.query_key_value.weight torch.Size([3072, 1024])
222 transformer.h.18.self_attention.query_key_value.bias torch.Size([3072])
223 transformer.h.18.self_attention.dense.weight torch.Size([1024, 1024])
224 transformer.h.18.self_attention.dense.bias torch.Size([1024])
225 transformer.h.18.post_attention_layernorm.weight torch.Size([1024])
226 transformer.h.18.post_attention_layernorm.bias torch.Size([1024])
227 transformer.h.18.mlp.dense_h_to_4h.weight torch.Size([4096, 1024])
228 transformer.h.18.mlp.dense_h_to_4h.bias torch.Size([4096])
229 transformer.h.18.mlp.dense_4h_to_h.weight torch.Size([1024, 4096])
230 transformer.h.18.mlp.dense_4h_to_h.bias torch.Size([1024])
231 transformer.h.19.input_layernorm.weight torch.Size([1024])
232 transformer.h.19.input_layernorm.bias torch.Size([1024])
233 transformer.h.19.self_attention.query_key_value.weight torch.Size([3072, 1024])
234 transformer.h.19.self_attention.query_key_value.bias torch.Size([3072])
235 transformer.h.19.self_attention.dense.weight torch.Size([1024, 1024])
236 transformer.h.19.self_attention.dense.bias torch.Size([1024])
237 transformer.h.19.post_attention_layernorm.weight torch.Size([1024])
238 transformer.h.19.post_attention_layernorm.bias torch.Size([1024])
239 transformer.h.19.mlp.dense_h_to_4h.weight torch.Size([4096, 1024])
240 transformer.h.19.mlp.dense_h_to_4h.bias torch.Size([4096])
241 transformer.h.19.mlp.dense_4h_to_h.weight torch.Size([1024, 4096])
242 transformer.h.19.mlp.dense_4h_to_h.bias torch.Size([1024])
243 transformer.h.20.input_layernorm.weight torch.Size([1024])
244 transformer.h.20.input_layernorm.bias torch.Size([1024])
245 transformer.h.20.self_attention.query_key_value.weight torch.Size([3072, 1024])
246 transformer.h.20.self_attention.query_key_value.bias torch.Size([3072])
247 transformer.h.20.self_attention.dense.weight torch.Size([1024, 1024])
248 transformer.h.20.self_attention.dense.bias torch.Size([1024])
249 transformer.h.20.post_attention_layernorm.weight torch.Size([1024])
250 transformer.h.20.post_attention_layernorm.bias torch.Size([1024])
251 transformer.h.20.mlp.dense_h_to_4h.weight torch.Size([4096, 1024])
252 transformer.h.20.mlp.dense_h_to_4h.bias torch.Size([4096])
253 transformer.h.20.mlp.dense_4h_to_h.weight torch.Size([1024, 4096])
254 transformer.h.20.mlp.dense_4h_to_h.bias torch.Size([1024])
255 transformer.h.21.input_layernorm.weight torch.Size([1024])
256 transformer.h.21.input_layernorm.bias torch.Size([1024])
257 transformer.h.21.self_attention.query_key_value.weight torch.Size([3072, 1024])
258 transformer.h.21.self_attention.query_key_value.bias torch.Size([3072])
259 transformer.h.21.self_attention.dense.weight torch.Size([1024, 1024])
260 transformer.h.21.self_attention.dense.bias torch.Size([1024])
261 transformer.h.21.post_attention_layernorm.weight torch.Size([1024])
262 transformer.h.21.post_attention_layernorm.bias torch.Size([1024])
263 transformer.h.21.mlp.dense_h_to_4h.weight torch.Size([4096, 1024])
264 transformer.h.21.mlp.dense_h_to_4h.bias torch.Size([4096])
265 transformer.h.21.mlp.dense_4h_to_h.weight torch.Size([1024, 4096])
266 transformer.h.21.mlp.dense_4h_to_h.bias torch.Size([1024])
267 transformer.h.22.input_layernorm.weight torch.Size([1024])
268 transformer.h.22.input_layernorm.bias torch.Size([1024])
269 transformer.h.22.self_attention.query_key_value.weight torch.Size([3072, 1024])
270 transformer.h.22.self_attention.query_key_value.bias torch.Size([3072])
271 transformer.h.22.self_attention.dense.weight torch.Size([1024, 1024])
272 transformer.h.22.self_attention.dense.bias torch.Size([1024])
273 transformer.h.22.post_attention_layernorm.weight torch.Size([1024])
274 transformer.h.22.post_attention_layernorm.bias torch.Size([1024])
275 transformer.h.22.mlp.dense_h_to_4h.weight torch.Size([4096, 1024])
276 transformer.h.22.mlp.dense_h_to_4h.bias torch.Size([4096])
277 transformer.h.22.mlp.dense_4h_to_h.weight torch.Size([1024, 4096])
278 transformer.h.22.mlp.dense_4h_to_h.bias torch.Size([1024])
279 transformer.h.23.input_layernorm.weight torch.Size([1024])
280 transformer.h.23.input_layernorm.bias torch.Size([1024])
281 transformer.h.23.self_attention.query_key_value.weight torch.Size([3072, 1024])
282 transformer.h.23.self_attention.query_key_value.bias torch.Size([3072])
283 transformer.h.23.self_attention.dense.weight torch.Size([1024, 1024])
284 transformer.h.23.self_attention.dense.bias torch.Size([1024])
285 transformer.h.23.post_attention_layernorm.weight torch.Size([1024])
286 transformer.h.23.post_attention_layernorm.bias torch.Size([1024])
287 transformer.h.23.mlp.dense_h_to_4h.weight torch.Size([4096, 1024])
288 transformer.h.23.mlp.dense_h_to_4h.bias torch.Size([4096])
289 transformer.h.23.mlp.dense_4h_to_h.weight torch.Size([1024, 4096])
290 transformer.h.23.mlp.dense_4h_to_h.bias torch.Size([1024])
291 transformer.ln_f.weight torch.Size([1024])
292 transformer.ln_f.bias torch.Size([1024])




8 base_model.model.model.decoder.layers.0.self_attn.v_proj.lora_A.default.weight   
9 base_model.model.model.decoder.layers.0.self_attn.v_proj.lora_B.default.weight   
12 base_model.model.model.decoder.layers.0.self_attn.q_proj.lora_A.default.weight  
13 base_model.model.model.decoder.layers.0.self_attn.q_proj.lora_B.default.weight  
28 base_model.model.model.decoder.layers.1.self_attn.v_proj.lora_A.default.weight  
29 base_model.model.model.decoder.layers.1.self_attn.v_proj.lora_B.default.weight  
32 base_model.model.model.decoder.layers.1.self_attn.q_proj.lora_A.default.weight  
33 base_model.model.model.decoder.layers.1.self_attn.q_proj.lora_B.default.weight  
48 base_model.model.model.decoder.layers.2.self_attn.v_proj.lora_A.default.weight  
49 base_model.model.model.decoder.layers.2.self_attn.v_proj.lora_B.default.weight  
52 base_model.model.model.decoder.layers.2.self_attn.q_proj.lora_A.default.weight  
53 base_model.model.model.decoder.layers.2.self_attn.q_proj.lora_B.default.weight  
68 base_model.model.model.decoder.layers.3.self_attn.v_proj.lora_A.default.weight  
69 base_model.model.model.decoder.layers.3.self_attn.v_proj.lora_B.default.weight  
72 base_model.model.model.decoder.layers.3.self_attn.q_proj.lora_A.default.weight  
73 base_model.model.model.decoder.layers.3.self_attn.q_proj.lora_B.default.weight  
88 base_model.model.model.decoder.layers.4.self_attn.v_proj.lora_A.default.weight  
89 base_model.model.model.decoder.layers.4.self_attn.v_proj.lora_B.default.weight  
92 base_model.model.model.decoder.layers.4.self_attn.q_proj.lora_A.default.weight  
93 base_model.model.model.decoder.layers.4.self_attn.q_proj.lora_B.default.weight  
108 base_model.model.model.decoder.layers.5.self_attn.v_proj.lora_A.default.weight 
109 base_model.model.model.decoder.layers.5.self_attn.v_proj.lora_B.default.weight 
112 base_model.model.model.decoder.layers.5.self_attn.q_proj.lora_A.default.weight 
113 base_model.model.model.decoder.layers.5.self_attn.q_proj.lora_B.default.weight 
128 base_model.model.model.decoder.layers.6.self_attn.v_proj.lora_A.default.weight 
129 base_model.model.model.decoder.layers.6.self_attn.v_proj.lora_B.default.weight 
132 base_model.model.model.decoder.layers.6.self_attn.q_proj.lora_A.default.weight 
133 base_model.model.model.decoder.layers.6.self_attn.q_proj.lora_B.default.weight 
148 base_model.model.model.decoder.layers.7.self_attn.v_proj.lora_A.default.weight 
149 base_model.model.model.decoder.layers.7.self_attn.v_proj.lora_B.default.weight 
152 base_model.model.model.decoder.layers.7.self_attn.q_proj.lora_A.default.weight 
153 base_model.model.model.decoder.layers.7.self_attn.q_proj.lora_B.default.weight 
168 base_model.model.model.decoder.layers.8.self_attn.v_proj.lora_A.default.weight 
169 base_model.model.model.decoder.layers.8.self_attn.v_proj.lora_B.default.weight 
172 base_model.model.model.decoder.layers.8.self_attn.q_proj.lora_A.default.weight 
173 base_model.model.model.decoder.layers.8.self_attn.q_proj.lora_B.default.weight 
188 base_model.model.model.decoder.layers.9.self_attn.v_proj.lora_A.default.weight 
189 base_model.model.model.decoder.layers.9.self_attn.v_proj.lora_B.default.weight 
192 base_model.model.model.decoder.layers.9.self_attn.q_proj.lora_A.default.weight 
193 base_model.model.model.decoder.layers.9.self_attn.q_proj.lora_B.default.weight 
208 base_model.model.model.decoder.layers.10.self_attn.v_proj.lora_A.default.weight
209 base_model.model.model.decoder.layers.10.self_attn.v_proj.lora_B.default.weight
212 base_model.model.model.decoder.layers.10.self_attn.q_proj.lora_A.default.weight
213 base_model.model.model.decoder.layers.10.self_attn.q_proj.lora_B.default.weight
228 base_model.model.model.decoder.layers.11.self_attn.v_proj.lora_A.default.weight
229 base_model.model.model.decoder.layers.11.self_attn.v_proj.lora_B.default.weight
232 base_model.model.model.decoder.layers.11.self_attn.q_proj.lora_A.default.weight
233 base_model.model.model.decoder.layers.11.self_attn.q_proj.lora_B.default.weight
"""

