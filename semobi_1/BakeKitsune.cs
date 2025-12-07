using System;
using Server.Items;
using Server.Mobiles;

namespace Server.Mobiles
{
	[CorpseName( "a Bake Kitsune corpse" )]
	public class BakeKitsune : BaseCreature
	{
		public override WeaponAbility GetWeaponAbility()	
            {
                  return WeaponAbility.BleedAttack;
            } 

		[Constructable]
		public BakeKitsune() : base( AIType.AI_Mage, FightMode.Closest, 10, 1, 0.2, 0.4 )
		{
			Name = "a Bake Kitsune";
			Body = 246;
			BaseSoundID = 0xE5;

			SetStr( 170, 220 );
			SetDex( 125, 145 );
			SetInt( 375, 425 );

			SetHits( 310, 350 );
			SetMana( 375, 425 );
			SetStam( 125, 145 );

			SetDamage( 32, 45 );

			SetDamageType( ResistanceType.Physical, 70 ); 
	         	SetDamageType( ResistanceType.Energy, 30 ); 

			SetResistance( ResistanceType.Physical, 40, 60 );
			SetResistance( ResistanceType.Fire, 70, 90 );
			SetResistance( ResistanceType.Cold, 40, 60 );
			SetResistance( ResistanceType.Poison, 40, 60 );
			SetResistance( ResistanceType.Energy, 40, 60 );

			SetSkill( SkillName.MagicResist, 80.0, 100.0 );
			SetSkill( SkillName.Tactics, 70.0, 90.0 );
			SetSkill( SkillName.Wrestling, 50.0, 55.0 );
			SetSkill( SkillName.Poisoning, 0.0, 0.0 );
			SetSkill( SkillName.Magery, 80.0, 90.0 );
			SetSkill( SkillName.Meditation, 85.0, 95.0 );
			SetSkill( SkillName.EvalInt, 80.0, 90.0 );

			Fame = 150;
			Karma = -150;
			
			Tamable = true;
			ControlSlots = 2;
			MinTameSkill = 80.7;
			
         PackGold( 700, 1000 ); 
         PackMagicItems( 1, 5 );
		 PackItem( new Bone( Utility.RandomMinMax( 5, 14 ) ));
		 PackReg( 5, 14 );
		 //TODO: Bonsai Seed
 
		}
		
		public override void GenerateLoot()
		{
			AddLoot( LootPack.MedScrolls, 2 );
		}
		public override Poison PoisonImmune{ get{ return Poison.Deadly; } }
		public override Poison HitPoison{ get{ return Poison.Deadly; } }
		public override FoodType FavoriteFood{ get{ return FoodType.Fish; } }
		public override int Meat{ get{ return 3; } }
		public override int Hides{ get{ return 30; } }
		public override HideType HideType{ get{ return HideType.Spined; } }


                public BakeKitsune( Serial serial ) : base( serial )
		{
		}

		public override void Serialize( GenericWriter writer )
		{
			base.Serialize( writer );

			writer.Write( (int) 0 ); // version
		}

		public override void Deserialize( GenericReader reader )
		{
			base.Deserialize( reader );

			int version = reader.ReadInt();
		}
	}
}