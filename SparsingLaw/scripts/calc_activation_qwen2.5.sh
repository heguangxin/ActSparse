model_path="/home/gxhe/models/models--Qwen--Qwen2.5-0.5B/snapshots/060db6499f32faf8b98477b0a26969ef7d8b9987"
input_file="/home/gxhe/workspace2/SparsingLaw/src/input.txt"
prune_strategy="pplp"
prune_arg="1.5"

OPT=""
OPT+=" --from-pretrained ${model_path}"
OPT+=" --input-file ${input_file}"
OPT+=" --prune-strategy ${prune_strategy}"
OPT+=" --prune-arg ${prune_arg}"

OPT+=" --output-image"

CMD="python3 /home/gxhe/workspace2/SparsingLaw/src/calc_activation_qwen2.5.py ${OPT}"

echo ${CMD}
${CMD}
